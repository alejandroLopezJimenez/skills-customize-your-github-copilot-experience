from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# In-memory store for items
items = {}
next_item_id = 1

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    response = {"item_id": item_id, **item}
    if q:
        response["query"] = q
    return response

@app.post("/items/")
def create_item(item: Item):
    global next_item_id
    item_id = next_item_id
    next_item_id += 1

    items[item_id] = item.dict()
    return {"item_id": item_id, **items[item_id]}

# Run the server with:
# uvicorn assignments.fastapi-rest-apis.starter-code:app --reload
