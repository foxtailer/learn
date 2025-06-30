from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from their_made.infrastructure.orm import metadata
from their_made.domain.model import Batch, OrderLine


def init_db():
    engine = create_engine("sqlite:////home/zoy/git/learn/courses/books/py_patterns/Chapter1/part_1/their_made/made.db")
    metadata.create_all(engine)
    return engine


db = init_db()
session = sessionmaker(bind=db)