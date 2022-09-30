from random import randint

from typing import Union

from fastapi import FastAPI

app = FastAPI()

todos = [
    {
        'id': 1
        'title': 'The first task',
    },
    {
        'id': 2
        'title': 'The second task'
    }
]


@app.get("/")
def read_root():
    return todos


@app.post("/todos")
def add_todo(title: str):
    id = randint(1000, 10000)

    todo = {
        'id': id,
        'title': title,
    }

    return {"id": id, "title": title}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
