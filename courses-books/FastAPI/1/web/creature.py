from fastapi import APIRouter, HTTPException

import service.creature as data 
from data.errors import Missing, Duplicate


router = APIRouter(prefix = '/creature')


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

