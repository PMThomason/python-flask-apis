from db import db
from sqlalchemy import Column, ForeignKey, Integer, String, Float, create_engine

class TagModel(db.Model):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    store_id = Column(String(), ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="tags")