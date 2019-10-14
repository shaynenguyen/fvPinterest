from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://fpvPinterest:ZLjSLzz0uuE6PxXy@localhost/fpvPinterest?charset=utf8mb4',
                        convert_unicode=True)

# From: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/
session = sessionmaker( autocommit  =   False,
                        autoflush   =   False,
                        bind        =   engine)()       # Session is a class

Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models
    Base.metadata.create_all(bind=engine)