FROM python:3.11-slim

WORKDIR /app
COPY service-b/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY service-b/app.py ./app.py

EXPOSE 5000
CMD ["python", "app.py"]
