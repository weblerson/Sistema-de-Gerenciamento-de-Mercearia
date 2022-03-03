from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = "root"
PASS = ""
HOST = "localhost"
DB = "antonio variedades"
PORT = "8000"

CONNECTION = f"mariadb+pymysql://{USER}:{PASS}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONNECTION, echo = False)

Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base