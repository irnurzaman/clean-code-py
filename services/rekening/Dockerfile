FROM python:3.8.11-slim

WORKDIR /app
ADD . .

RUN pip install -r requirements.txt

ENV DB_DATABASE bds
ENV DB_HOST localhost
ENV DB_USER bds
ENV DB_PASSWORD password
ENV REKENING_HOST localhost
ENV REKENING_PORT 8001

EXPOSE 8001

ENTRYPOINT python main.py