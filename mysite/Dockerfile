# syntax=docker/dockerfile1.4
FROM --platform=$BUILDPLATFORM python:3.10-alpha AS builder
EXPOSE 8000
WORKDIR /app

# install system dependencies
RUN apk update
RUN apk add \
    build-base \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev 



# Install Python dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt --platform=$BUILDPLATFORM

# copy rest of application codes to container 
COPY  . /app

#run server
ENTRYPOINT [ "python3" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000" ]



