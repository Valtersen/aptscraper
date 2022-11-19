FROM python

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

COPY aptapi /usr/src/app/aptapi

COPY aptscraper /usr/src/app/aptscraper

COPY start.py /usr/src/app

COPY scrapy.cfg /usr/src/app

ENV USERNAME=debug
ENV PASSWORD=debug

EXPOSE 5432
EXPOSE 6800
