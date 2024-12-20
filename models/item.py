from db import db
from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class ItemModel(db.Model):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(Float(precision=2), unique=False, nullable=False)
    store_id = Column(Integer, ForeignKey("stores.id"),  unique=False, nullable=False)
    store = db.relationship("StoreModel", back_populates="items")

    

    