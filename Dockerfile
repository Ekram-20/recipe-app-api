FROM python:3.9-alpine3.13
LABEL maintainer="londonappdeveloper.com"

# to see the output of the application logs
ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

#all subsequent instructions (e.g., COPY, RUN, CMD, etc.) in the Dockerfile will be executed.
WORKDIR /app
EXPOSE 8000

# this is the default if not set in docker-compose.yml
ARG DEV=false

# some thinks no need for venv but it is good to have
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# I think like active the virtual env
ENV PATH="/py/bin:$PATH"

USER django-user