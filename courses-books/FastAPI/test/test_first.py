import os
import pytest
from model import Creature
from data.errors import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data.init import curs, conn
from data import creature


curs.execute("""
    CREATE TABLE creature(
        name UNIQUE,
        description, 
        country, 
        area, 
        aka
    )
""")


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="Yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    )


def test_create(sample):
    resp = creature.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        creature.create(sample)


def test_get_exists(sample):
    resp = creature.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        creature.get_one("boxturtle")


def test_modify(sample):
    sample.country = "GL" # Greenland!
    resp = creature.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    bob: Creature = Creature(
            name="bob",
            description="some guy", 
            country="ZZ",
            aka="buka",
            area="world"
    )

    with pytest.raises(Missing):
        creature.modify(bob.name, bob)

def test_delete(sample):
    resp = creature.delete(sample.name)
    assert resp is None

def test_delete_missing(sample):
    with pytest.raises(Missing):
        creature.delete(sample.name)

