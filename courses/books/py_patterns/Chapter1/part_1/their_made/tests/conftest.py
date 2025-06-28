import sys
from pathlib import Path

# Get the parent directory of the script file
parent_dir = Path(__file__).resolve().parent.parent
print(parent_dir)
# Add it to sys.path
sys.path.append(str(parent_dir))


import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from orm import metadata, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()