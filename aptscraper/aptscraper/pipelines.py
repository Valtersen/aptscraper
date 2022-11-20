# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.exc import IntegrityError
# useful for handling different item types with a single interface
from sqlalchemy.orm import Session
from . import models


class AptscraperPipeline:

    def __init__(self):
        self.engine = models.db_engine()
        models.create_tables(self.engine)

        self.session = Session(bind=self.engine)

    def process_item(self, item: dict, spider):

        apartment = models.Apartment()
        for key, value in item.items():
            if value == 'limited':
                value = 2
            setattr(apartment, key, value)

        try:
            self.session.add(apartment)
            self.session.commit()

        except IntegrityError:
            self.session.rollback()

        finally:
            self.session.close()

        return item

