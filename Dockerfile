FROM python:3.6
MAINTAINER Ahmed Dhanani (ahmed.dhanani26@gmail.com)

RUN mkdir -p /var/loc
COPY . /var/loc

WORKDIR /var/loc

RUN apt-get update
RUN apt-get install -y apt-utils
RUN pip install -r requirements.txt

EXPOSE 8000

CMD python app.py
