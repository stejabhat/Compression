import os
import shutil
import py7zr
import zipfile
import json
from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render


def handle_uploaded_zip(request):
    """
    Uploads a ZIP file, extracts it, recompresses it with high compression, and provides the smaller file for download.
    """
    if request.method == 'POST' and request.FILES.get('zip_file'):
        uploaded_zip = request.FILES['zip_file']
        zip_filename = uploaded_zip.name
        base_name, _ = os.path.splitext(zip_filename)

        # Define paths
        zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)
        extract_path = os.path.join(settings.MEDIA_ROOT, f"{base_name}_extracted")
        recompressed_filename = f"{base_name}_compressed.7z"
        recompressed_path = os.path.join(settings.MEDIA_ROOT, recompressed_filename)

        # Ensure media directory exists
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        # Save the uploaded ZIP file
        with open(zip_path, 'wb+') as destination:
            for chunk in uploaded_zip.chunks():
                destination.write(chunk)

        # Extract the ZIP file
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
        except zipfile.BadZipFile:
            return JsonResponse({"error": "Invalid ZIP file."}, status=400)

        # Compress the extracted folder using 7z (high compression)
        try:
            with py7zr.SevenZipFile(recompressed_path, 'w', filters=[{'id': py7zr.FILTER_LZMA2, 'preset': 9}]) as archive:
                archive.writeall(extract_path, arcname=base_name)
        except Exception as e:
            return JsonResponse({"error": f"Compression error: {e}"}, status=500)

        # Cleanup: Delete extracted folder and original ZIP file
        shutil.rmtree(extract_path)
        os.remove(zip_path)

        # Debug: Print the saved file path
        print(f"Compressed file saved at: {recompressed_path}")

        # Return JSON response with file name for automatic download
        return JsonResponse({"compressed_file": recompressed_filename})

    return render(request, 'upload_zip.html')


def download_file(request, filename):
    """
    Allows the user to download the compressed file automatically.
    """
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    # Debug: Print the file path
    print(f"Trying to download: {file_path}")

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response
    else:
        return JsonResponse({"error": f"File not found: {file_path}"}, status=404)
import os
import shutil
import py7zr
from django.conf import settings
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import render

def upload_and_compress_folder(request):
    """
    Handles folder uploads (as multiple files), reconstructs the folder structure,
    compresses it to 7z, and allows the user to download the compressed file.
    """
    if request.method == 'POST' and request.FILES.getlist('folder_files'):
        files = request.FILES.getlist('folder_files')

        # Ensure a unique folder name to prevent overwriting
        folder_name = request.POST.get("folder_name", "uploaded_folder")
        upload_path = os.path.join(settings.MEDIA_ROOT, folder_name)

        # Remove old folder if it exists
        if os.path.exists(upload_path):
            shutil.rmtree(upload_path)
        os.makedirs(upload_path)

        # Save uploaded files while maintaining folder structure
        for file in files:
            sub_path = file.name  # Retains sub-folder structure if provided
            file_path = os.path.join(upload_path, sub_path)

            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create necessary subdirectories
            with open(file_path, 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        # Compress the folder using 7z
        compressed_filename = f"{folder_name}_compressed.7z"
        compressed_path = os.path.join(settings.MEDIA_ROOT, compressed_filename)

        try:
            with py7zr.SevenZipFile(compressed_path, 'w', filters=[{'id': py7zr.FILTER_LZMA2, 'preset': 9}]) as archive:
                archive.writeall(upload_path, arcname=folder_name)
        except Exception as e:
            return JsonResponse({"error": f"Compression error: {e}"}, status=500)

        # Cleanup: Remove extracted folder after compression
        shutil.rmtree(upload_path)

        # Return JSON response with file name for automatic download
        return JsonResponse({"compressed_file": compressed_filename})

    return render(request, 'upload.html')


def download_file(request, filename):
    """
    Allows the user to download the compressed file automatically.
    """
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response
    else:
        return JsonResponse({"error": f"File not found: {file_path}"}, status=404)
