FROM ubuntu:latest
LABEL maintainer="kartoch@gmail.com"
ARG MY_NAME
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install Flask
RUN apt-get install -y curl
ADD hello.py /home/hello.py
ADD static /home/static
RUN echo "${MY_NAME}" > /home/static/name.txt
WORKDIR /home
CMD ["/usr/bin/python3", "hello.py"]
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:5000/healthz || exit 1
VOLUME /home/static/
USER 1000
EXPOSE 5000
