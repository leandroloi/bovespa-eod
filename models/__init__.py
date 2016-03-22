# -*- coding: utf-8 -*-
import logging
from sqlalchemy import DateTime, engine_from_config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, Query


__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

Base = declarative_base()
DBSession = scoped_session(sessionmaker())
logger = logging.getLogger(__name__)


def initialize_database(settings):
    """Called by the app on startup to setup bindings to the DB"""
    engine = engine_from_config(settings, 'sqlalchemy.')

    if not DBSession.registry.has():
        DBSession.configure(bind=engine)
        Base.metadata.bind = engine
        Base.metadata.create_all(engine)


def save_obj(obj):
    """
        Save any mapped object to database
    :param obj:
    :return:
    """
    session = DBSession()
    try:
        session.add(obj)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def save_bulk_objs(objs=[]):
    session = DBSession()
    try:
        # for obj in objs:
        #     session.bulk_insert_mappings(obj)
        session.add_all(objs)
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()



def todict(self):
    """Method to turn an SA instance into a dict so we can output to json"""

    def convert_datetime(value):
        """We need to treat datetime's special to get them to json"""
        if value:
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return ""

    for col in self.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(self, col.name))
        else:
            value = getattr(self, col.name)

        yield(col.name, value)


def iterfunc(self):
    """Returns an iterable that supports .next()
        so we can do dict(sa_instance)
    """
    return self.__todict__()


def fromdict(self, values):
    """Merge in items in the values dict into our object
       if it's one of our columns
    """
    for col in self.__table__.columns:
        if col.name in values:
            setattr(self, col.name, values[col.name])


# Setup the SQLAlchemy database engine
Base.query = DBSession.query_property(Query)
Base.__todict__ = todict
Base.__iter__ = iterfunc
Base.fromdict = fromdict


