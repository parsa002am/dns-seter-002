from sqlalchemy import   Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
DataBaseBase = declarative_base()

class DNS(DataBaseBase):
    __tablename__ = 'DNS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    primary_dns = Column(String, nullable=False)
    secondary_dns = Column(String, nullable=False)