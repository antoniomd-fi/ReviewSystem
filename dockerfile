# Base Image
FROM python:3.8-slim

WORKDIR /app

COPY review_system_backend/requirements.txt .

# Instal dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY review_system_backend/review_system /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
