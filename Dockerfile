FROM python:3.11.5

# set work directory
RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements/base.txt .
RUN pip install -r base.txt

# copy files
COPY ./toolbox /code/

# Expose port
EXPOSE 8000