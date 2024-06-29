from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .Models import DataBaseBase


DATABASE_URL = f"sqlite:///data002.db"

DB_engine = create_engine(DATABASE_URL)
DataBaseBase.metadata.create_all(DB_engine)
Session = sessionmaker(bind=DB_engine)