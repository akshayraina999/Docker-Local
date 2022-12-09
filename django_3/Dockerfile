FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
