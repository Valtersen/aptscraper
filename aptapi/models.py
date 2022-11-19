from sqlalchemy import create_engine, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Integer, String, Date, DateTime, Float, Text)

from . import settings


Base = declarative_base()


def db_engine():
    engine = create_engine(f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
    Base.metadata.create_all(engine)
    return engine


def create_tables(engine):
    Base.metadata.create_all(engine)


class Apartment(Base):
    __tablename__ = 'apartment'

    id = Column(Integer, primary_key=True)
    url = Column(String)
    city = Column(String)
    title = Column(String)
    description = Column(Text)
    posted = Column(DateTime)
    location = Column(String)
    owner_id = Column(Integer)
    owner_name = Column(String)
    owner_phone = Column(String)
    price = Column(Float)

    # attributes
    forrentbyhousing = Column(String)
    unittype = Column(String)
    numberbedrooms = Column(Float)
    numberbathrooms = Column(Float)
    agreementtype = Column(String)
    dateavailable = Column(Date)
    petsallowed = Column(Integer)
    areainfeet = Column(Integer)
    furnished = Column(Integer)
    laundryinunit = Column(Integer)
    laundryinbuilding = Column(Integer)
    dishwasher = Column(Integer)
    fridgefreezer = Column(Integer)
    airconditioning = Column(Integer)
    yard = Column(Integer)
    balcony = Column(Integer)
    smokingpermitted = Column(Integer)
    gym = Column(Integer)
    pool = Column(Integer)
    concierge = Column(Integer)
    twentyfourhoursecurity = Column(Integer)
    bicycleparking = Column(Integer)
    storagelocker = Column(Integer)
    elevator = Column(Integer)
    wheelchairaccessible = Column(Integer)
    braillelabels = Column(Integer)
    audioprompts = Column(Integer)
    barrierfreeentrancesandramps = Column(Integer)
    visualaids = Column(Integer)
    accessiblewashroomsinsuite = Column(Integer)
    hydro = Column(Integer)
    heat = Column(Integer)
    water = Column(Integer)
    cabletv = Column(Integer)
    internet = Column(Integer)
    numberparkingspots = Column(Integer)
