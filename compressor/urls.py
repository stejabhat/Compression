from django.urls import path
from .views import handle_uploaded_zip, download_file,upload_and_compress_folder

urlpatterns = [
    path('compress-zip/', handle_uploaded_zip, name='compress_zip'),
    path('download/<str:filename>/', download_file, name='download_file'),
     path('compress-folder/', upload_and_compress_folder, name='compress_folder'),
]
