from .init import curs, IntegrityError
from model import Explorer
from .errors import Missing, Duplicate


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row

    return Explorer(
            name=name, 
            country=country,
            description=description
    ) 


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict() if explorer else None


def get_one(name: str) -> Explorer:
    qry = "SELECT * FROM explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)

    if not (row := curs.fetchone()):
        raise Missing(msg=f"Explorer {name} not found.")

    return row_to_model(row)


def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(explorer: Explorer) -> Explorer:
    qry = """
        INSERT INTO explorer (name, country, description)
        VALUES (:name, :country, :description)
    """
    params = model_to_dict(explorer)

    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(
                msg=f'Explorer {explorer.name} already exist'
        )
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    qry = """
        UPDATE explorer
            SET 
            country=:country,
            name=:name,
            description=:description
        WHERE name=:name_orig
    """

    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    
    if cursor.rowcount == 1:
        return get_one(explorer.name)
    else:
        raise Missing(msg=f"Explorer {name} not found")


def delete(explorer: Explorer) -> bool:
    qry = "DELETE FROM explorer WHERE name = :name"
    params = {"name": explorer.name}
    curs.execute(qry, params)
    
    if cursor.rowcount != 1:
        raise Missing(msg="Explorer {name} not found")


