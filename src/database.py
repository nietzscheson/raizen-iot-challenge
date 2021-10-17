import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

env = os.environ

db_session = scoped_session(sessionmaker())

engine = create_engine(
    f"postgresql://{env['DATABASE_USER']}:{env['DATABASE_PASS']}@{env['DATABASE_HOST']}:5432/{env['DATABASE_NAME']}"
)


def init_session():
    db_session.configure(bind=engine)

    from model import Base

    Base.metadata.create_all(bind=engine)
