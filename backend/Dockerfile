FROM python:3.12.1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
