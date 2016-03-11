import logging

from sqlalchemy import engine_from_config, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker, mapper
from sqlalchemy.ext.declarative import declarative_base

from zope.sqlalchemy import ZopeTransactionExtension

log = logging.getLogger(__name__)

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
DBMetadata = MetaData()
Base = declarative_base()


def add(*args, **kwargs):
    return DBSession.add(*args, **kwargs)


def execute(*args, **kwargs):
    return DBSession.execute(*args, **kwargs)


def query(*args, **kwargs):
    return DBSession.query(*args, **kwargs)


def scalar(*args, **kwargs):
    return DBSession.scalar(*args, **kwargs)


class ReflectedTable(object):
    """Base class for database objects that are mapped to tables by reflection.
    """
    __tablename__ = None


class Event(ReflectedTable):
    __tablename__ = 'events'


def map_tables(to_reflect):
    for _class in to_reflect:
        log.info('Reflecting {0} from table {1}'
                 .format(_class, _class.__tablename__))
        table = Table(_class.__tablename__, DBMetadata, autoload=True)
        mapper(_class, table)


def includeme(config):
    settings = config.registry.settings
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    DBMetadata.bind = engine
    to_reflect = (
        Event,
    )
    map_tables(to_reflect)
