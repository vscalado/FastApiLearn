from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column('id',Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), nullable=False)
    slug = Column('slug', String(100), nullable=False)

    