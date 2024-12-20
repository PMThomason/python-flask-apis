from db import db
from sqlalchemy import Column, Integer, String, Float, create_engine

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    # Define 1-many relationship
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")
