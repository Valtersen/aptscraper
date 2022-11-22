from sqlalchemy.orm import Session
import json
import settings
import models


async def get_session():
    engine = models.db_engine()
    session = Session(bind=engine)
    return session


async def process_objects(apts):
    resp = [vars(apt) for apt in apts]
    [apt.pop('_sa_instance_state') for apt in resp]
    return json.dumps(resp, default=str, indent=4)


async def get_all_apts(session: Session):
    return session.query(models.Apartment).all()


async def get_apt_by_id(session: Session, id: int):
    return session.query(models.Apartment).filter(models.Apartment.id == id).all()


async def get_apt_filters(session: Session, **kwargs):

    queue = session.query(models.Apartment)

    for kwarg, kvalue in kwargs.items():

        # check if true/false attributes
        if kwarg in settings.apt_unit_attributes_1 \
                or kwarg in settings.apt_unit_attributes_2:
            kwargs[kwarg] = 1 if kvalue == 'True' else 0 if kvalue == 'False' else kvalue
            queue = queue.filter(getattr(models.Apartment, kwarg) == kwargs[kwarg])

        # check if range attribute
        if 'min_' in kwarg and kwarg.replace('min_', '') in settings.apt_unit_attributes_2:
            kwarg = kwarg.replace('min_', '')
            queue = queue.filter(getattr(models.Apartment, kwarg) >= kvalue)

        if 'max_' in kwarg and kwarg.replace('max_', '') in settings.apt_unit_attributes_2:
            kwarg = kwarg.replace('max_', '')
            queue = queue.filter(getattr(models.Apartment, kwarg) <= kvalue)

    return queue.all()
