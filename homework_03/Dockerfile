# docker build -t my-fastapi-app:latest -f ./homework_03/Dockerfile .
# docker run -p 8080:8000 my-fastapi-app:latest
FROM python:3.9-buster

WORKDIR /fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]