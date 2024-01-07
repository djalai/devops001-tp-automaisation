FROM python:3.10

WORKDIR /app

COPY app.py /app/main.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
