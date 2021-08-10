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
ENV NASABAH_HOST localhost
ENV NASABAH_PORT 8000

EXPOSE 8000

ENTRYPOINT python main.py