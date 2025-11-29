from fastapi import FastAPI

# http://127.0.0.1:8000/openapi.json
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

app = FastAPI()

# @app.post()
# @app.put()
# @app.delete()
# @app.options()
# @app.head()
# @app.patch()
# @app.trace()
@app.get("/{id}")
async def root(id: int|str):
    return {"id": id}
    # return {"message": "Hello World"}