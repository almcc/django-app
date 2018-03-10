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
  - `python manage.py createsuperuser`
6. Run the web-server:
  - `gunicorn core.wsgi --reload`
