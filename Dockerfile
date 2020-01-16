FROM python:3.7-slim

RUN pip install cookiecutter

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
