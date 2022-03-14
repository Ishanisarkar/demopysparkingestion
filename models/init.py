
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .orm import Base

def create_session_from_url(uri):
  engine = create_engine(uri)
  maker = sessionmaker(engine)
  return engine, maker


def db_session():
  from config import make_settings
  _, DEFAULT_SESSION_MAKER = create_session_from_url(make_settings().db_uri)
  return scoped_session(DEFAULT_SESSION_MAKER)

def create_all(engine: Engine = None):
  from config import make_settings
  if engine is None:
    engine, _ = create_session_from_url(make_settings().db_uri)
  Base.metadata.create_all(engine)
  return engine


if __name__ == "__main__":
  create_all()