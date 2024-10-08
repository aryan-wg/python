from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = "sqlite:///./database.db"

engine = create_engine(DB_URL,connect_args = {"check_same_thread":False})

session_local = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


