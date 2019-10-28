from sqlalchemy import Column, Integer, String
from .database import Base

class Images(Base):
    __tablename__ = 'images'
    index   = Column(Integer, primary_key=True)
    name    = Column('name',String)
    url     = Column('url',String)
    width   = Column('width',Integer)
    height  = Column('height',Integer)

    def __init__(self, name, url, width, height):
        self.name   = name
        self.url    = url
        self.width  = width
        self.height = height
    

    # def __repr__(self):
        # return '<Image %r>' % (self.name)