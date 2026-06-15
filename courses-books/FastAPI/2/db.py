from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
    sessionmaker,
    Session
)
from sqlalchemy import create_engine

from data import books_data, users_data


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    name: Mapped[str]
    email: Mapped[str]


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def populate_db():
    db = SessionLocal()

    try:
        # Convert dicts to SQLAlchemy objects
        books = [Book(**book) for book in books_data]
        users = [User(**user) for user in users_data]

        # Add to session
        db.add_all(books)
        db.add_all(users)

        # Save changes
        db.commit()

        print("Database populated!")

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


'''
https://google.com
postgresql://user:password@localhost/db
sqlite:///test.db
'''


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    populate_db()

