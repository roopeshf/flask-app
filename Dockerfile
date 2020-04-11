FROM python:3.7-alpine
RUN mkdir /app
COPY app_start.py /app/
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 /app/app_start.py


