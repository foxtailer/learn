from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import registry

import model

mapper_registry = registry()
metadata = mapper_registry.metadata

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)


def start_mappers():
    mapper_registry.map_imperatively(model.OrderLine, order_lines)
