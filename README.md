# Django App

An example Django app including:

- Gunicorn Web server
- Whitenoise
- dj-database-url
- PostgreSQL

- CSS & JS Framework
- JSON API
- JWT Auth
- Celery Worker
- Caching

# Running

1. Create the python virtual environment:
  - `python3 -m venv vnev`
  - `. venv/bin/activate`
  - `pip install -r requirements.txt`
2. Define the environment variables:
  - `. ./develop.env`
3. Run the background services with docker:
  - `docker-compose up -d`
4. Migrate the database
  - `python manage.py migrate`
5. Create a super user
  - `python manage.py createsuperuser`
6. Run the web-server:
  - `gunicorn core.wsgi --reload`
