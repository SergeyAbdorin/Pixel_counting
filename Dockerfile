FROM python:3.9.6

WORKDIR /app

COPY requirements.txt ./

RUN pip install --disable-pip-version-check -r requirements.txt

COPY pixel/ ./

EXPOSE 80