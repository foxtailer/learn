from contextlib import asynccontextmanager

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import init_db
import requests


@asynccontextmanager
async def lifespan(app_: FastAPI):
    await init_db()
    print('Bot is ready')
    yield
    # 🔴 Code after `yield` (not shown here) would run on shutdown


app = FastAPI(title='To Do App', lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/api/tasks/{tg_id}")
async def tasks(tg_id: int):
    user = await requests.add_user(tg_id)
    return await requests.get_tasks(user.id)


@app.get("/api/main/{tg_id)")
async def profile(tg_id: int):
    user = await requests.add_user(tg_id)
    completed_tasks_count = await requests.get_completed_tasks_count(user.id)
    return {'completedTasks': completed_tasks_count}

