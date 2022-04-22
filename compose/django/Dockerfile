FROM python:3.8.3-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev

COPY requirements.txt /app

RUN python3 -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver" , "0.0.0.0:8000"]
