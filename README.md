# Blog Website (Django Recap)

This repository is a small Django blog project created as a learning exercise to reinforce Django fundamentals and explore new concepts. It implements a minimal blog with posts, templates, static assets, and basic URL routing.

## Purpose & Learning Goals

- Practice building a Django project from start to finish.
- Reinforce understanding of Django project structure (settings, URLs, WSGI/ASGI).
- Work with Django apps, models, views, templates, and static files.
- Handle migrations and simple admin configuration.
- Learn how to wire templates and static assets into pages and create simple list/detail views.

This project was created as a learning task — it's intentionally small and focused on reinforcing skills rather than being production-ready.

## Repository Structure

Top-level files
- `manage.py` - Django management script.
- `requirements.txt` - Python dependencies used while developing (check before installing).

Main folders
- `blog_website/` - Django project configuration (settings, URLs, WSGI/ASGI).
- `blogs/` - Django app that contains models, views, URLs, admin and tests related to the blog posts.
- `templates/` - HTML templates. Contains `base.html` and `posts/` templates for the home and post detail pages.
- `static/` - Static assets like CSS. Includes `css/base.css` used by templates.

Example tree (trimmed):

- `blog_website/`
  - `settings.py`
  - `urls.py`
  - `wsgi.py` / `asgi.py`
- `blogs/`
  - `models.py` (Post model and related migrations)
  - `views.py` (list and detail views)
  - `urls.py` (app URL patterns)
  - `admin.py`
- `templates/`
  - `base.html`
  - `posts/`
    - `home.html`
    - `post_detail.html`
- `static/`
  - `css/base.css`

## Quickstart — Local Development

These instructions assume you have Python 3.8+ and virtualenv or venv available. Adjust commands for your environment.

1. Clone the repository (if you haven't already):

```bash
git clone https://github.com/peterkahumu/Blog_website-Django-Recap.git
cd blog_website
```

2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. (Optional) Create a superuser to access the admin site:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Visit the app in your browser:

- Home / posts list: http://127.0.0.1:8000/ (or as configured in `blogs.urls`)
- Admin: http://127.0.0.1:8000/admin/

## Tests

There is a `blogs/tests.py` file for app tests. Run tests with:

```bash
python manage.py test blogs
```

If tests are minimal or missing, consider adding unit tests for models and views as a next step.

## Configuration Notes

- Check `blog_website/settings.py` for DEBUG, ALLOWED_HOSTS, database configuration, and static/template settings.
- This project likely uses SQLite by default (the Django default). For production use, configure a robust database and secret management.

## Troubleshooting

- If dependencies fail to install, check the Python version and consider upgrading pip: `python -m pip install --upgrade pip`.
- If migrations fail, ensure the database file is writable (for SQLite) and there are no conflicting migrations.

## License

Please refer to [LICENSE](LICENSE) for more details.


