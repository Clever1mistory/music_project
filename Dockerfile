FROM python:3.11

WORKDIR /app

COPY ../requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY .. /app

WORKDIR /app/ref_system

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "catalog.wsgi:application"]