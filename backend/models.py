from sqlalchemy import Column, Integer, String
from .database import Base

class Images(Base):
    __tablename__ = 'images'
    index   = Column(Integer, primary_key=True)
    name    = Column('name',String, unique=True)
    width   = Column('width',Integer, unique=True)
    height  = Column('height',Integer, unique=True)

    def __init__(self, name=None, width=None, height=None):
        self.name   = name
        self.width  = width
        self.height = height

    # def __repr__(self):
        # return '<Image %r>' % (self.name)