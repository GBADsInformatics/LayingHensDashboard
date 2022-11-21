# Base image - tried a few others, this one was the easiest and most resilient
FROM python:3.10.0-slim-buster

# Specify root directory in image
WORKDIR /app/dash

# Installing python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy dash files to image
COPY . /app/dash

# Setting env
ENV AUTH0_REDIRECT=/dash
ENV DEBUG=FALSE

# Specifying the dashboard command
CMD ["waitress-serve","--port=8051","--call","wsgi:returnApp"]

