# CHEAT SHEET: https://www.pythonsheets.com/notes/python-sqlalchemy.html

from sqlalchemy.engine.url import URL
import sys
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        JSON, Text, String, Enum, PrimaryKeyConstraint)
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.inspection import inspect
from sqlalchemy_utils import database_exists, create_database #pip install sqlalchemy-utils


Base = declarative_base()

DIALECT = "mysql"
DRIVER = "mysqlconnector"

MYSQL_DB = {
    'username': 'ajeeb',
    'password': 'Welcome1',
    'host': 'localhost',
    'port': 3306
}

DB_NAME = "playground"

MYSQL_DRIVER = f"{DIALECT}+{DRIVER}"


class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(String(255), primary_key=True)
    reg_no = Column(String(255), primary_key=True)
    name = Column(String(255))

    def __repr__(self):
        items = (f"{k}={v!r}" for k, v in self.__dict__.items())
        return "{}({})".format(type(self).__name__, ", ".join(items))

class Session:
    def __init__(self):
        url = URL.create(MYSQL_DRIVER, **MYSQL_DB) # dialect+driver://username:password@host:port
        engine = create_engine(f"{url}/{DB_NAME}", echo=False)
        if not database_exists(engine.url):
            create_database(engine.url)
        Base.metadata.create_all(engine)
        self._session = scoped_session(sessionmaker(bind=engine))
    def __enter__(self):
        return self._session
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._session.remove()


def get_entry_if_exists(session, model, entry):
    primary_keys = get_primary_keys(model)
    query = session.query(model)
    for key in primary_keys:
        result = query.filter(getattr(model, key) == entry.get(key)).first()
        if result:
            return result

def add_initial_entries(model, entries):
    with Session() as session:
        for entry in entries:
            item = get_entry_if_exists(session, model, entry)
            if not item:
                session.add(model(**entry))
        session.commit()


def get_primary_keys(model):
    '''
    returns all primary keys in a table
    '''
    return [key.name for key in inspect(model).primary_key]


def _print_new_dirty_deleted(session, msg):
    print(f"\n--- {msg} ---")
    print(f"\n\tsession.new: {session.new}")
    print(f"\n\tsession.dirty: {session.dirty}")
    print(f"\n\tsession.deleted: {session.deleted}")

def test_new_dirty_deleted(model):
    kwargs = {'id': '4321', 'reg_no': 3214 ,'name': 'lexus'}
    with Session() as session:
        _print_new_dirty_deleted(session, "Before adding a new entry")
        entry = get_entry_if_exists(session, model, kwargs)
        if entry:
            session.delete(entry)
            session.commit()
            _print_new_dirty_deleted(session, "After deleting existing entry")
        session.add(model(**kwargs))
        _print_new_dirty_deleted(session, "After adding a new entry")
        session.commit()
        _print_new_dirty_deleted(session, "After committing add")
        entry = get_entry_if_exists(session, model, kwargs)
        _print_new_dirty_deleted(session, "After getting the added entry")
        entry.name = "Lexus 125"
        session.add(entry)
        _print_new_dirty_deleted(session, "After updating new entry")
        session.commit()
        _print_new_dirty_deleted(session, "After committing update")
        entry = get_entry_if_exists(session, model, kwargs)
        _print_new_dirty_deleted(session, "After getting the updated entry")
        session.delete(entry)
        _print_new_dirty_deleted(session, "After deleting new entry")
        _print_new_dirty_deleted(session, "After committing delete")



if __name__ == '__main__':
    kwargs =[
        {'id': '8043', 'reg_no': 1234 ,'name': 'Kia Seltos'},
        {'id': '9999', 'reg_no': 3213 ,'name': 'Benz'},
        {'id': '9893', 'reg_no': 9043 ,'name': 'i10'},
        {'id': '3821', 'reg_no': 8942 ,'name': 'nano'}
    ]
    add_initial_entries(Vehicle, kwargs)
    test_new_dirty_deleted(Vehicle)
