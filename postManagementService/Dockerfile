FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

USER root

RUN microdnf update && microdnf install -y python38 python38-pip python38-devel && microdnf clean all

RUN python3.8 -m ensurepip --upgrade

WORKDIR /src/app

COPY . /src/app

COPY requirements.txt /src/app/

EXPOSE 50053

RUN python3.8 -m pip install -r requirements.txt

CMD ["python3.8", "server.py"]

