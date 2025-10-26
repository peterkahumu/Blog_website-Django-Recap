## Repository Structure
# Blog Website (Django Recap)

This repository is a small Django blog project created as a learning exercise to reinforce Django fundamentals and explore new concepts. It implements a minimal blog with posts, templates, static assets, and basic URL routing.

## Purpose & Learning Goals

- Practice building a Django project from start to finish.
- Reinforce understanding of Django project structure (settings, URLs, WSGI/ASGI).
- Work with Django apps, models, views, templates, and static files.
- Handle migrations and simple admin configuration.
- Learn how to wire templates and static assets into pages and create simple list/detail views.

This project was created as a learning task — it's intentionally small and focused on reinforcing skills rather than being production-ready.

## Project Status

- Status: Learning / demo project (not production hardened).
- Last update: 2025-10-26 — README expanded with changelog and contribution notes.

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
  - `registration/`
    - `register.html` (user registration template - if used by the project)
- `static/`
  - `css/base.css`

Note: There is a registration template located at `templates/registration/register.html` (the project includes the template file; wiring up the view/URL for user registration may require additional view code if not already present).

## Quickstart — Local Development

These instructions assume you have Python 3.8+ and virtualenv or venv available. Adjust commands for your environment.

1. Clone the repository (if you haven't already):

```bash
git clone https://github.com/peterkahumu/Blog_website-Django-Recap.git
cd blog_website
```

2. Create and activate a virtual environment (recommended):

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

Tip: If you add a registration view or third-party package (e.g., django-allauth), ensure you update `INSTALLED_APPS` and the template paths in `settings.py`.

## Tests

There is a `blogs/tests.py` file for app tests. Run tests with:

```bash
python manage.py test
```

If tests are minimal or missing, consider adding unit tests for models and views as a next step.

## Configuration Notes

- Check `blog_website/settings.py` for DEBUG, ALLOWED_HOSTS, database configuration, and static/template settings.
- This project uses ``postgresql` for the database. For production use, configure a robust database and secret management.
- If static files don't appear during development, ensure `STATICFILES_DIRS`/`STATIC_URL` are set and run `python manage.py collectstatic` only for production settings.

## Changelog / Recent updates

- 2025-10-26 — Set up user authentication (register, login, logout.)

## Contributing

This repository is primarily a personal learning project, but contributions are welcome. Suggested low-risk contributions:

- Add or expand unit tests for models and views.
- Improve templates and styling (responsive design).
- Add pagination, search, or tagging features for posts.
- Add documentation for any new features or changes.

If you open a PR, include a short description of changes and a brief test plan.

## Troubleshooting

- If dependencies fail to install, check the Python version and consider upgrading pip: `python -m pip install --upgrade pip`.
- If migrations fail, ensure the database file is writable (for SQLite) and there are no conflicting migrations.
- If templates or static files are not found, confirm `TEMPLATES` and `STATICFILES_DIRS` settings in `blog_website/settings.py`.

## License

This repository includes a `LICENSE` file at the project root. Check it for license terms.

## Acknowledgements

Created as a learning exercise to practice Django fundamentals and pick up new concepts.

## Contact

If you want help extending this project (Docker, CI, auth, REST API), open an issue or request changes via a pull request. I'm happy to help add the next feature and include tests and documentation.


