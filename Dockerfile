FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

COPY requirements.txt /app

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" ]
