from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
        q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fix@*@$")] = None
    ):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}

    if q:
        results.update({"q": q})

    return results


# http://localhost:8000/items/?q=foo&q=bar
@app.get("/items2/")
async def read_items(q: Annotated[list[str] | None, Query(alias="item-query")] = None):
    query_items = {"q": q}
    return query_items