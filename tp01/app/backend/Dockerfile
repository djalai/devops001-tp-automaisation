FROM tiangolo/uwsgi-nginx-flask:python3.10

WORKDIR /app

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
