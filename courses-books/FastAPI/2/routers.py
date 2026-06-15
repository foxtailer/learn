from fastapi import APIRouter, Depends
from bson import ObjectId

from stypes import AllBookM, AllUserM, BookM, UserM
from db import get_db, User, Book, Session
from nosqldb import user_collection


router = APIRouter()


@router.get("/allbooks", response_model=list[AllBookM])
async def all_books(
        db: Session = Depends(get_db)
):
    return db.query(Book).all()


@router.get("/allusers", response_model=list[AllUserM])
def read_users(
        db: Session = Depends(get_db)
):
    users = db.query(User).all()
    return users


@router.post("/user")
def add_new_user(
    user: UserM,
    db: Session = Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# http -v localhost:8000/user/9 name="Alice9" email="alice@gmail.com"
@router.post("/user/{user_id}")
def update_user(
    user_id: int,
    user: UserM,
    db: Session = Depends(get_db),
):
    db_user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/user", response_model=UserM)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.delete("/user")
def delete_user(
    user_id: int, db: Session = Depends(get_db)
):
    db_user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )

    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted"}


@router.get("/nosqlusers")
def nsread_users() -> list[UserM]:
    return [user for user in user_collection.find()]


@router.post("/nosqluser")
def nscreate_user(user: UserM):
    result = user_collection.insert_one(
        user.model_dump(exclude_none=True)
    )

    return {"result": str(result.inserted_id)}


@router.get("/nosqluser")
def nsget_user(user_id: str):
    db_user = user_collection.find_one(
        {
            "_id": ObjectId(user_id)
                if ObjectId.is_valid(user_id)
                else None
        }
    )

    if db_user is None:
        raise HTTPException(
        status_code=404,
        detail="User not found"
    )

    return UserM.model_validate(db_user) 

