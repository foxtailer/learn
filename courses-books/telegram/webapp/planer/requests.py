from pydantic import BaseModel, ConfigDict
from sqlalchemy import select, update, delete, func

from models import async_session, User, Task


class TaskSchema(BaseModel):
    id: int
    user: int
    text: str
    active: bool

    model_config = ConfigDict(from_attributes=True)


async def add_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            return user
        
        new_user = User(tg_id=tg_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user
    

async def get_tasks(user_id):
    async with async_session() as session:
        tasks = await session.scalars(
            select(Task).where(Task.user == user_id, Task.active == True)
        )

        serialized_tasks = [
            TaskSchema.model_validate(t).model_dump() for t in tasks
        ]

        return serialized_tasks


async def get_completed_tasks_count(user_id: int):
    async with async_session() as session:
        stmt = select(func.count(Task.id)).where(
            Task.completed == True,
            Task.user_id == user_id
        )
        return await session.scalar(stmt)

