from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    text : str = None
    is_done : bool = False


items = []

@app.get("/")
def root():
    return {"Witaj": "Kolego"}


@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items


@app.get("/items/{item_id}")
def get_item(item_id : int) -> str:
    item = items[item_id]
    return item