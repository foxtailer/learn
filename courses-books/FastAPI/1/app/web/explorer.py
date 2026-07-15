from fastapi import APIRouter, HTTPException

import service.explorer as data
from data.errors import Missing, Duplicate
from model import Explorer


router = APIRouter(prefix = '/explorer')


@router.get('')
@router.get('/')
async def creatures():
    return data.get_all()


@router.get('/{name}')
@router.get('/{name}/')
async def creature(name: str):
    try:
        return data.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(explorer: Explorer) -> Explorer:
    try:
        return service.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch("/")
def modify(name: str, explorer: Explorer) -> Explorer:
    try:
        return service.modify(name, explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.delete("/{name}", status_code=204)
def delete(name: str):
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

