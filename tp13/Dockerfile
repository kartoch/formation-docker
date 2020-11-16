FROM ubuntu:20.04
LABEL maintainer="kartoch@gmail.com"
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
RUN pip3 install Flask
ADD hello.py /home/hello.py
ADD static /home/static
ENV FLASK_APP=hello.py
WORKDIR /home

