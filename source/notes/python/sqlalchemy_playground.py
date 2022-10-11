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


def _get_entry(session, model, entry):
    primary_keys = get_primary_keys(model)
    query = session.query(model)
    for key in primary_keys:
        result = query.filter(getattr(model, key) == entry.get(key)).first()
        if result:
            return result

def _clear(session, model, entry):
    primary_keys = get_primary_keys(model)
    query = session.query(model)
    for key in primary_keys:
        result = query.filter(getattr(model, key) == entry.get(key)).first()
        if result:
            session.delete(result)

def _clear_all(model, entries):
    with Session() as session:
        for entry in entries:
            _clear(session, model, entry)
        session.commit()

def add_initial_entries(model, entries):
    with Session() as session:
        for entry in entries:
            session.add(model(**entry))
        session.commit()


def get_primary_keys(model):
    '''
    returns all primary keys in a table
    '''
    return [key.name for key in inspect(model).primary_key]


def _print_new_dirty_deleted(session, msg):
    print(f"\n{msg}:")
    print(f"\tsession.new: {session.new}, session.dirty: {session.dirty}, "
          f"session.deleted: {session.deleted}")


def test_new_dirty_deleted(model):
    kwargs01 = {'id': '4321', 'reg_no': 3214 ,'name': 'lexus'}
    kwargs02 = {'id': '3213', 'reg_no': 1432 ,'name': 'new lexus'}
    with Session() as session:
        _clear_all(model, [kwargs01, kwargs02])
        _print_new_dirty_deleted(session, "Before adding a new entry")
        session.add(model(**kwargs01))
        _print_new_dirty_deleted(session, "After adding entry #01")
        session.add(model(**kwargs02))
        _print_new_dirty_deleted(session, "After adding entry #02")
        session.commit()
        _print_new_dirty_deleted(session, "After commit")
        entry01 = _get_entry(session, model, kwargs01)
        entry02 = _get_entry(session, model, kwargs02)
        _print_new_dirty_deleted(session, "After getting entry #01")
        entry01.name = "Lexus 125"
        session.add(entry01)
        entry02.name = "New Lexus 125"
        session.add(entry02)
        _print_new_dirty_deleted(session, "After updating entry #01")
        session.commit()
        _print_new_dirty_deleted(session, "After commit")
        entry = _get_entry(session, model, kwargs01)
        _print_new_dirty_deleted(session, "After getting entry #01")
        session.delete(entry)
        entry = _get_entry(session, model, kwargs02)
        # a query will implicitly flush changes to the db. So, the  above delete
        # entry will no longer exists in session.deleted
        _print_new_dirty_deleted(session, "After getting entry #02")
        session.delete(entry)
        _print_new_dirty_deleted(session, "After deleting entry #01")
        _print_new_dirty_deleted(session, "After commit")


def test_query_and_flush(model):
    kwargs01 = {'id': '4321', 'reg_no': 3214 ,'name': 'lexus'}
    kwargs02 = {'id': '3213', 'reg_no': 1432 ,'name': 'new lexus'}
    with Session() as session:
        _clear_all(model, [kwargs01, kwargs02])
        session.add(model(**kwargs01))
        session.add(model(**kwargs02))
        # 2 items must be there in the session.new.
        print(f"\n{session.new}") # IdentitySet([Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x10e217370>, id='4321', reg_no=3214, name='lexus'), Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x10e2bcf40>, id='3213', reg_no=1432, name='new lexus')])
        # mysql> select * from vehicle;
        # Empty set (0.00 sec)
        session.flush() # means, communicated to db and db maintains them as pending operations in a transaction.
        # mysql> select * from vehicle;
        # Empty set (0.00 sec)
        print(f"\n{session.new}") # IdentitySet([])
        # not that as soon as session is flushed, session.new is also gone.
        # This doesn't mean, data is gone. let's try to get data.
        entry01 = _get_entry(session, model, kwargs01)
        print(f"{entry01.id} {entry01.name}") # 4321 lexus
        session.commit()
        print(f"{entry01.id} {entry01.name}") # 4321 lexus !! YES YOU CAN STILL QUERY. COMMIT JUST COMMIT THE TRANSACTION.

        _clear_all(model, [kwargs01, kwargs02])
        session.add(model(**kwargs01))
        session.add(model(**kwargs02))
        print(f"\n{session.new}")
        entry01 = _get_entry(session, model, kwargs01)
        # at this point, session.new will not contain anything as a 
        # session.query will implicitly flush changes to db.
        print(f"\n{session.new}")


def test_expunge(model):
    kwargs01 = {'id': '4321', 'reg_no': 3214 ,'name': 'lexus'}
    kwargs02 = {'id': '3213', 'reg_no': 1432 ,'name': 'Toyota'}
    kwargs03 = {'id': '9899', 'reg_no': 3322 ,'name': 'Audi'}
    with Session() as session:
        _clear_all(model, [kwargs01, kwargs02])
        session.add(model(**kwargs01))
        session.add(model(**kwargs02))
        _print_new_dirty_deleted(session, "Before expunge") # session.new: IdentitySet([Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x108805370>, id='4321', reg_no=3214, name='lexus'), Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x1088aaf40>, id='3213', reg_no=1432, name='Toyota')])session.dirty: IdentitySet([]), session.deleted: IdentitySet([])
        session.expunge_all()
        _print_new_dirty_deleted(session, "After expunge") # session.new: IdentitySet([]), session.dirty: IdentitySet([]), session.deleted: IdentitySet([])
        session.commit() # nothing to commit to db
        # mysql> select * from vehicle;
        # Empty set (0.00 sec)
        session.add(model(**kwargs01))
        session.add(model(**kwargs02))
        session.commit()
        entry01 = _get_entry(session, model, kwargs01)
        entry02 = _get_entry(session, model, kwargs02)
        entry01.name = "new-lexus"
        entry02.name = "new-toyota"
        session.add(entry01)
        session.add(entry02)
        _print_new_dirty_deleted(session, "Before expunge") # session.dirty: IdentitySet([Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x103425a90>, reg_no='3214', name='new-lexus', id='4321'), Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x103425040>, reg_no='1432', name='new-toyota', id='3213')])
        session.expunge(entry01)
        _print_new_dirty_deleted(session, "After expunge") #session.dirty: IdentitySet([Vehicle(_sa_instance_state=<sqlalchemy.orm.state.InstanceState object at 0x103425040>, reg_no='1432', name='new-toyota', id='3213')])
        session.commit()
        # mysql> select * from vehicle;
        # +------+--------+------------+
        # | id   | reg_no | name       |
        # +------+--------+------------+
        # | 3213 | 1432   | new-toyota |
        # | 4321 | 3214   | lexus      |
        # +------+--------+------------+
        # 2 rows in set (0.00 sec)


        

if __name__ == '__main__':
    kwargs =[
        {'id': '8043', 'reg_no': 1234 ,'name': 'Kia Seltos'},
        {'id': '9999', 'reg_no': 3213 ,'name': 'Benz'},
        {'id': '9893', 'reg_no': 9043 ,'name': 'i10'},
        {'id': '3821', 'reg_no': 8942 ,'name': 'nano'}
    ]
    _clear_all(Vehicle, kwargs)
    # add_initial_entries(Vehicle, kwargs)
    # test_new_dirty_deleted(Vehicle)
    # test_query_and_flush(Vehicle)
    test_expunge(Vehicle)
