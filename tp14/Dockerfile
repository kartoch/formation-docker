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
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
HEALTHCHECK --interval=10s --timeout=3s CMD curl -f http://localhost:5000/healthz || exit 1
VOLUME /home/static/
ENV FLASK_ENV="development"
ENV FLASK_APP="hello.py"
USER 1000
EXPOSE 5000
