FROM python:3

WORKDIR /usr/src/app


ENV DOCKER_BUILDKIT=0
ENV COMPOSE_DOCKER_CLI_BUILD=0


COPY ./requirements.txt /usr/src/app/requirements.txt

COPY ./aptapi //usr/src/app/aptapi

COPY ./aptscraper /usr/src/app/aptscraper

COPY ./scrapy.cfg /usr/src/app/

RUN pip install -r requirements.txt

CMD ["uvicorn aptapi.main:app; curl -X POST http://localhost:6800/schedule.json -d project=aptscraper -d spider=page_scraper"]
