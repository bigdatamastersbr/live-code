from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_endpoint = "PREENCHA_AQUI"

engine = create_engine(database_endpoint, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

