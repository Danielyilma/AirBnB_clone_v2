'''database storage for hbnb clone'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    '''database storage class'''

    __engine = None
    __session = None
    _cls = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ), pool_pre_ping=True
        )
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        This function retrieves all instances of a given class
        or all classes from a database session and stores them
        in a dictionary with keys formatted as "ClassName.instance_id".
        """
        result = {}
        key = ''
        if cls is None:
            for cls in self._cls:
                key = cls.__name__ + '.'
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key += obj.id
                    result[key] = obj
        else:
            key = cls.__name__ + '.'
            objs = self.__session.query(cls).all()
            for obj in objs:
                key += obj.id
                result[key] = obj
        return result

    def new(self, obj):
        '''adding object to the session before commiting'''
        self.__session.add(obj)

    def save(self):
        '''saving object to the database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''deleting object'''
        if obj is not None:
            self.__session.delete(obj)
        return

    def reload(self):
        '''createing sesssion instance to interact to the database'''
        Base.metadata.create_all(self.__engine)
        Scope_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(Scope_session)
        self.__session = Session()

    def close(self):
        '''close the session instance and closing the connection'''
        self.__session.close()
