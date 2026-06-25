from model import Creature


# fake data, replaced in Chapter 10 by a real database and SQL
_creatures = [
    Creature(name="Yeti",
             aka="Abominable Snowman",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan"),
    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch"),
    ]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name.lower() == name.lower():
            return _creature
    return None

def create(creature: Creature) -> Creature:
    return creature

def replace(id, creature: Creature) -> Creature:
    return creature

def modify(id, creature: Creature) -> Creature:
    return creature

def delete(id, creature: Creature) -> bool:
    return creature


