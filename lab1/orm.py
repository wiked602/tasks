import sqlite3
from sqlalchemy import Column,String,Integer,ForeignKey,DateTime,Float,create_engine,Text,REAL
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


Base = declarative_base()

class directors(Base):
    __tablename__ = 'directors'
    name = Column(String)
    id = Column(Integer, primary_key= True)
    gender = Column(Integer)
    uid = Column(Integer)
    department = Column(String)

class movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key= True)
    original_title =  Column(String)
    budget = Column(Integer)
    popularity = Column(Integer)
    release_date = Column(Text)
    revenue = Column(Integer)
    title = Column(Text)
    vote_average = Column(REAL)
    vote_count = Column(Integer)
    overview = Column(Text)

def setup_database(database_path="sqlite:///movie.sqlite"):
    engine = create_engine(database_path)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()



