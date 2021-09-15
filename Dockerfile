FROM python:3.9.6

RUN mkdir /code

COPY requirements.txt /code

RUN pip install --disable-pip-version-check -r /code/requirements.txt

COPY . /code

CMD python /code/pixel/manage.py runserver 0:8000 