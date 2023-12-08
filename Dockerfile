# -*- coding: utf-8 -*-
# Use a Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the entire Flask app to the container
COPY . /app

# Expose the port where the app runs
EXPOSE 5000

# Set the command to start the Flask app
CMD ["python", "-m", "app.routes"]