FROM python:3.14-alpine3.22

WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache build-base postgresql-dev libffi-dev openssl-dev musl-dev \
    && pip install --no-cache-dir -r requirements.txt
COPY ./app/* .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
