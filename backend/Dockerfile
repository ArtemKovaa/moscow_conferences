FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py migrate

ENTRYPOINT [ "uwsgi", "uwsgi.ini" ]
