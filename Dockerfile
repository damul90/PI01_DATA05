# FROM python:3.9
# COPY . /app
# RUN pip install no-cache-dir -r requirements.txt
# ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
COPY . /app