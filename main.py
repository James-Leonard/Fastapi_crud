from random import randint

from typing import Union

from fastapi import FastAPI

app = FastAPI()

todos = [
    {
        'id': 1,
        'title': 'The first task',
    },
    {
        'id': 2,
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


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str):
    todo = next(key for key in todos if key['id'] == todo_id)
    todo['title'] = title

    return {"id": todo['id'], "title": todo['title']}
