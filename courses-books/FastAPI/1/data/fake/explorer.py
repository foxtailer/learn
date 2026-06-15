from model import Explorer


# fake data, replaced in Chapter 10 by a real database and SQL
_explorers = [
    Explorer(name="Claude Hande",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="Myopic machete man"),
    ]


def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

def create(explorer: Explorer) -> Explorer:
    return explorer

def replace(id, explorer: Explorer) -> Explorer:
    return explorer

def modify(id, explorer: Explorer) -> Explorer:
    return explorer

def delete(id, explorer: Explorer) -> bool:
    return explorer

