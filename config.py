from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION = f"sqlite:///mercearia.db"

engine = create_engine(CONNECTION, echo = False)

Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()