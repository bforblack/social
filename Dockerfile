FROM registry.access.redhat.com/ubi8/ubi-minimal:latest

USER root

RUN microdnf update && microdnf install -y python38 python38-pip python38-devel && microdnf clean all

RUN python3.8 -m ensurepip --upgrade

RUN microdnf install -y gcc gcc-c++ make automake autoconf libtool

WORKDIR /src/app

COPY social_oculus /src/app

COPY requirements.txt /src/app/

ENV PYTHONPATH "${PYTHONPATH}:/src/app"

RUN python3.8 -m pip install -r requirements.txt

CMD ["python3.8", "server.py"]

