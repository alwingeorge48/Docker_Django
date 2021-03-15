from python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /Django-SFTP

ADD . /Django-SFTP

COPY ./requirements.txt /Django-SFTP/requirements.txt

RUN pip install -r requirements.txt

COPY . /Django-SFTP