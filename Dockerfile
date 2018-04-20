FROM python:3.6

EXPOSE 8000

ADD . /opt/app

WORKDIR /opt/app

RUN pip install -r requirements-dev.txt

CMD gunicorn core.wsgi --bind=0.0.0.0:8000 --log-level=DEBUG --workers=1
