# Django App

An example Django app including:

- Gunicorn Web server
- Whitenoise
- dj-database-url
- PostgreSQL
- Boostrap, Bootswatch and django-bootstrap4
- JSON API
- Celery Worker

Todo:

- Linting
- JWT Auth
- BDD Testing
- Invoke targets for common tasks
- Tidy up URL definitions

The Django project is called 'core' and it includes an single app called
'base' which includes a couple of standard items the most projects would
need.

# Running

Note: There command line tools and services that you will
      need to have installed on your system:

 - docker
 - docker-compose
 - python3
 - openssl
 - envsubst

1. Create the python virtual environment:
  - `python3 -m venv vnev`
  - `. ./venv/bin/activate`
  - `pip install -r requirements.txt`
2. Define the environment variables:
  - `. ./develop.env.starter`
3. Save your environment variables for later:
  - `envsubst < develop.env.template > develop.env`
  -  next time for steps 2 & 3 you can just use `. ./develop.env`, but be
     careful not to commit the `develop.env` file. It is the `.gitignore`
     just encase.
3. Run the background services with docker:
  - `docker-compose up -d`
4. Migrate the database
  - `python manage.py migrate`
5. Create a super user
  - `python manage.py createsuperuser --email admin@example.com --username admin`
6. Run the web-server in it's own shell:
  - `gunicorn core.wsgi --reload --bind=127.0.0.1:8000`
7. Run a celery worker in another shell:
  - `celery -A core worker -l info`
8. Run the celery monitor flower in another shell:
  - `celery flower -A core --address=127.0.0.1 --port=5555`
