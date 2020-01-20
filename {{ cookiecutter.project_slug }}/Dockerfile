FROM python:3.7-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    vim git

ARG USER=docker
ARG UID=1000
ARG GID=1000

RUN addgroup --gid "$GID" "$USER" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --uid "$UID" \
    --gid "$GID" \
    "$USER"

USER $USER
