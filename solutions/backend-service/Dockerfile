FROM python:3.8-alpine
WORKDIR /src
COPY requirements.txt .
COPY ./src /src
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python server.py
 