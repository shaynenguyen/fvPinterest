from sqlalchemy import Column, Integer, String
from database import Base

class Images(Base):
    __tablename__ = 'images'
    id      = Column(Integer, primary_key=True)
    name    = Column(String(200), unique=True)
    width   = Column(Integer, unique=True)
    height  = Column(Integer, unique=True)

    def __init__(self, name=None, width=None, height=None):
        self.name   = name
        self.width  = width
        self.height = height

    def __repr__(self):
        return '<Image %r>' % (self.name)