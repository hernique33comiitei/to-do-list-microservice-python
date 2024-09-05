from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    completed = Column(Boolean, default=False)

def get_engine(database_url):
    return create_engine(database_url)

def get_session_local(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def setup_database(database_url):
    engine = get_engine(database_url)
    Base.metadata.create_all(engine)
    SessionLocal = get_session_local(engine)
    return engine, SessionLocal

def defaultDatabase() -> Session:
    DATABASE_URL = os.getenv('DATABASE_URL')
    engine, SessionLocal = setup_database(DATABASE_URL)
    return SessionLocal()