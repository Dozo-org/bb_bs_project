FROM python:3.8.5
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD gunicorn BBBS_project.wsgi:application --bind 0.0.0.0:7000
