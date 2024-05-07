FROM python:3.11

RUN apt-get update

WORKDIR /guniapp

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8000
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "--workers=2", "main:app"]