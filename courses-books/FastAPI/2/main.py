from fastapi import FastAPI

from routers import router


app = FastAPI()
app.include_router(router)


@app.get("/")
async def home():
    return "Hello"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

