FROM ubuntu:latest
LABEL maintainer="kartoch@gmail.com"
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install Flask
ADD hello.py /home/hello.py
ADD static /home/static
WORKDIR /home

