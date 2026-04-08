*📊 Project Overview*

This project provides a simple, efficient interface for compressing files and folders:

Upload ZIP files → Extract and recompress to a smaller size.
Upload folders → Compress into a .7z archive.
Automatic download → File downloads after compression.
Progress bar → Tracks upload and download status.
Built with Django, Python, JavaScript, HTML, and CSS
🗂️ Project Structure
```
Compression/
├── media/                  # Stores uploaded files
├── static/                 # CSS, JS, Images
├── templates/              # HTML templates
├── myapp/                  # Django app
│   ├── views.py            # Core logic for compression
│   ├── urls.py             # URL mappings
├── manage.py               # Django project manager
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
```
🚀 Installation & Setup
1. Clone the Repository
```
git clone https://github.com/stejabhat/Compression.git
cd Compression
```
2. Create a Virtual Environment
```
python -m venv env
source env/bin/activate       # Windows: env\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Apply Migrations
```
python manage.py migrate
```
5. Run the Server
```
python manage.py runserver

```
Open 
```
http://127.0.0.1:8000/

```
in your browser.

**🔍 Usage**

Upload a ZIP file → Extracts and recompresses to .7z.
Upload a folder → Compresses into .7z.
Automatic download → Compressed file downloads automatically.
Progress bar → Visual feedback during upload/download.
**📦 Dependencies**
Django
py7zr

Install using:
```
pip install django py7zr
```
**🤝 Contributing**
***Fork the repository***
Create a new branch
```
git checkout -b feature-name
```
Commit changes
```
git commit -m "Add feature"
```
Push to GitHub
```
git push origin feature-name
```
Open a Pull Request

📝 Notes

Ensure 7-Zip is installed if handling .7z files outside Python.

Large file uploads depend on server settings (DATA_UPLOAD_MAX_MEMORY_SIZE in Django).
