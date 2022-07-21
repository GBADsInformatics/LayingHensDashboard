FROM python:3.8-slim-buster



WORKDIR /app/dash


ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt .
RUN pip install -r requirements.txt
# COPY requirements.txt /tmp/apireq

# RUN \
#     pip install -r /tmp/apireq
# RUN python -m pip install -r requirements.txt

EXPOSE 3000

COPY . /app/dash

# CMD ["python","wsgi.py"]
CMD ["flask", "run"]

