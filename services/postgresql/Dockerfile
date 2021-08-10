FROM postgres:13.3-alpine

ADD init.sql /docker-entrypoint-initdb.d

ENV POSTGRES_USER bds
ENV POSTGRES_PASSWORD password

EXPOSE 5432