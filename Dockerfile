FROM python:3
COPY ./add /opt/add
WORKDIR /opt
ENTRYPOINT ["python3"]
