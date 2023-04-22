FROM python:3.9-slim-buster

WORKDIR /dash_application

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8058

CMD ["python3", "dash_application_final.py"]


