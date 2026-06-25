from model import Creature
from .init import conn, curs, IntegrityError
from .errors import Missing, Duplicate


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row

    return Creature(
            name=name,
            description=description,
            country=country,
            area=area,
            aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.model_dump()


def get_one(name: str) -> Creature:
    qry = "SELECT * FROM creature WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)

    if not (row := curs.fetchone()):
        raise Missing(msg=f'Creature {name} is missing')

    return row_to_model(row)


def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    curs.execute(qry)
    rows = list(curs.fetchall())

    return [row_to_model(row) for row in rows]


def create(creature: Creature):
    qry = """
          INSERT INTO creature VALUES
          (:name, :description, :country, :area, :aka)
          """
    params = model_to_dict(creature)

    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(
                msg=f"Creature {creature.name} already exists"
        )

    return get_one(creature.name)


def modify(name: str, creature: Creature) -> Creature:
    if not (name and creature): return None
    qry = """
        UPDATE creature
        SET name=:name,
            country=:country,
            description=:description,
            aka=:aka,
            area=:area
        WHERE name=:name_origin
    """

    params = model_to_dict(creature)
    params["name_origin"] = creature.name
    curs.execute(qry, params)

    if curs.rowcount == 1:
        return get_one(creature.name)
    else:
        raise Missing(msg=f"Creature {name} not found")


def delete(name: str):
    qry = "DELETE FROM creature WHERE name = :name"
    params = {"name": name}
    curs.execute(qry, params)

    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")


