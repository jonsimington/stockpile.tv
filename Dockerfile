FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt


RUN apt-get update
RUN apt-get install curl
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash
RUN apt-get install nodejs
RUN npm install

ADD node_modules /code
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN node_modules/bower/bin/bower install

RUN python manage.py makemigrations
RUN python manage.py migrate

# Collect static files and move to /static
RUN mkdir /static
RUN python manage.py collectstatic
ADD . /code/
