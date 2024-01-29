"""
The database storage engine setup
"""
from os import getenv
from models.base_model import Base
from sqlalchemy import MetaData, create_engine
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

# the connection string setup for connecting mysql to sqlalchemy
CONNECTION_STRING = "mysql+mysqldb://{}:{}@{}/{}?charset=utf8mb4".\
    format(getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
           getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB'))

class DBStorage:
    """An object that handles setting up the database"""
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine(CONNECTION_STRING, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        
    def all(self, cls=None):
        """ Query all objects from the current database session """
        classes = {"State": State, "Amenity": Amenity, "City": City,
                   "User": User, "Place": Place, "Review": Review
                   }
        result = {}
        if cls:
            if isinstance(cls, str):
                cls = classes[cls]
            if cls in classes.values():
                objects = self.__session.query(cls).all()
                for obj in objects:
                    key = f'{type(obj).__name__}.{obj.id}'
                    result[key] = obj
                return result
        else:
            for c in classes.values():
                objects = self.__session.query(c).all()
                for obj in objects:
                    key = f'{type(obj).__name__}.{obj.id}'
                    result[key] = obj
            return result
 
    def new(self, obj):
        """add instance to current database session"""
        self.__session.add(obj)
    
    def save(self):
        """ save current session to database"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """
        delete data from database
        """
        if obj:
            self.__session.delete(obj)
        
    def reload(self):
        """Reload database"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """A method closing a a session"""
        self.__session.remove()