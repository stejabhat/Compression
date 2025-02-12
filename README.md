# Compression
ZIP & Folder Compressor Web App
A web application built with Django that allows users to upload ZIP files or folders, compress them using 7z high compression, and download the compressed file. It includes progress tracking for both upload and download.

Features
✅ Upload ZIP files and recompress them to a smaller size
✅ Upload entire folders, compress them, and download as .7z
✅ Automatic download of the compressed file after completion
✅ Progress bar for file upload
✅ Built with Django, JavaScript, and 7z compression

Tech Stack
Backend: Django, Python
Frontend: HTML, CSS, JavaScript
Compression: py7zr (7-Zip for Python)
Storage: Local file system
Installation & Setup
1️⃣ Clone the Repository
sh
Copy
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Create a Virtual Environment
sh
Copy
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
3️⃣ Install Dependencies
sh
Copy
pip install -r requirements.txt
4️⃣ Apply Migrations
sh
Copy
python manage.py migrate
5️⃣ Run the Server
sh
Copy
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.

Usage
Upload a ZIP file → The system extracts and recompresses it to a smaller size.
Upload a folder → The system compresses it into a .7z archive.
Automatic Download → Once the process completes, the compressed file will download automatically.
Progress Bar → Tracks the upload status.
Screenshots
Add screenshots of your app UI here.

Project Structure
php
Copy
📂 your-project-folder/
│-- 📂 media/              # Stores uploaded files
│-- 📂 static/             # CSS, JS, Images
│-- 📂 templates/          # HTML templates
│-- 📂 myapp/              # Django app
│   │-- views.py           # Core logic for compression
│   │-- urls.py            # URL mappings
│-- manage.py              # Django project manager
│-- requirements.txt       # Required Python packages
│-- README.md              # Project documentation
Dependencies
Install required packages using:

sh
Copy
pip install django py7zr
Contributing
Fork the repo
Create a new branch (git checkout -b feature-name)
Commit changes (git commit -m "Added feature")
Push to GitHub (git push origin feature-name)
Open a Pull Request
