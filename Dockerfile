FROM python:3
COPY add /opt
WORKDIR /opt
ENTRYPOINT ["python3"]
