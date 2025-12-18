Django Portfolio (main)

Tech Stack:
- Backend: Python 3.x, Django 5.2
- Frontend: HTML5, CSS3, Bootstrap 5.3, JavaScript
- Database: SQLite (default), configurable to PostgreSQL/MySQL
- Image Handling: Pillow (for image processing)
- Deployment: Ready for Heroku, AWS, or other platforms

Quick start:

1. Create and activate a virtual environment (Windows example):

   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt

3. Apply migrations and create superuser (optional):

   python manage.py migrate
   python manage.py createsuperuser

4. Run the development server:

   python manage.py runserver

5. Open http://127.0.0.1:8000 in your browser.

Profile image:
- Place the provided `ib_p.jpg` in the project root (it already is). On first load the site will copy it into `media/profile/ib_p.jpg` so it appears on the home page.

Uploading works:
- Use the upload form on the home page to add work images. Uploaded files will be stored under the `media/works/` directory.

Bulk loading image URLs:
- Add image URLs (one per line) to `image_urls.txt` and run the management command:

   python manage.py load_image_urls

This command will attempt to download each URL and create entries in the database.

Notes:
- Development server serves media files when `DEBUG=True`.
- To change the description text, edit `main/templates/index.html` and replace the placeholder 'Your Name' and description paragraph.
