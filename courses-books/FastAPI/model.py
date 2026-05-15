from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


class Explorer(BaseModel):
    name: str
    country: str
    description: str


class User(BaseModel):
    name: str
    hash_: str

