from datetime import timedelta
import os
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model import User

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as service
else:
    from service import user as service

from data.errors import Missing, Duplicate


ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix = "/user")


# This dependency makes a post to "/user/token"
# (from a form containing a username and password)
# and returns an access token.
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")


def unauthed():
    raise HTTPException(
        status_code=401,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
        )


@router.get("/register")
def register_user(name: str, password: str):
    try:
        if service.get_one(name):
            raise HTTPException(status_code=400, detail="User already exists")
            return {"message": "User already esists"} 
    except:
            return {"message": "Error"} 

    hashed_password = service.get_hash(password)

    data = {
        "name": name,
        "hash_": hashed_password
    }
    
    service.create(User(**data))

    return {"message": "User created successfully"}


# This endpoint is directed to by any call that has the
# oauth2_dep() dependency:
# http -f POST http://127.0.0.1:8000/user/token username=nami password=12345
@router.post("/token")
async def create_access_token(
    form_data: OAuth2PasswordRequestForm =  Depends()
):
    """Get username and password from OAuth form,
        return access token"""

    user = service.auth_user(form_data.username, form_data.password)

    if not user:
        unauthed()

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.name}, expires=expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


# http GET http://127.0.0.1:8000/user/token Authorization:"Bearer <token>"
@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    """Return the current access token"""
    return {"token": token}


# --- previous CRUD stuff

@router.get("/")
def get_all() -> list[User]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> User:
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("/")
def modify(name: str, user: User) -> User:
    try:
        return service.modify(name, user)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


# http -f DELETE http://127.0.0.1:8000/user/nami Authorization:"Bearer <token>"
@router.delete("/{name}")
def delete(name: str, token: str = Depends(oauth2_dep)) -> None:
    if (name_ := service.get_jwt_username(token)):
        if name == name_:
            try:
                return service.delete(name)
            except Missing as exc:
                raise HTTPException(status_code=404, detail=exc.msg)
            return {'result': 'done'}
    return {'result': 'broke'}

