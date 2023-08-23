from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World!"


@app.post("/api/")
def read_item(prefix: Union[str, None] = None):
    if (prefix == "0915"):
        return "Globe"
    elif (prefix == "0920"):
        return "Smart"
    return "Unknown"
