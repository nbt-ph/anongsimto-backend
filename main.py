from typing import Union
from fastapi import FastAPI

app = FastAPI()

# TODO: setup database connection

ALLOWED_CARRIERS = ["globe", "smart", "sun",
                    "dito", "tm", "tnt" "cherry", "gomo"]


@app.get("/")
# hello world!
def read_root():
    return "Hello World!"


@app.get("/api/")
# test endpoint for homework #1
def read_item(prefix: Union[str, None] = None):
    if (prefix == "0915"):
        return "Globe"
    elif (prefix == "0920"):
        return "Smart"
    elif (prefix == "0928"):
        return "Smart"
    return "Unknown"


@app.post("/api/loadPrefixData")
# upsert prefix and carrier data for one pair
# input: object(prefix, carrier)
# TODO: update data type
def read_item(carrier: Union[str, None] = None):
    return "Hello World!"


@app.post("/api/loadPrefixesData")
# upsert pairs of prefix and carrier data
# input: object(prefix, carrier)[]
# TODO: update data type
def read_item(carrier: Union[str, None] = None):
    return "Hello World!"


@app.get("/api/getCarrierPrefixes")
# get the prefixes from given carrier
# input: carrier: string
# output: prefixes: string[]
def read_item(carrier: Union[str, None] = None):
    return "Hello World!"


@app.get("/api/getCarrierFromPrefix")
# get the carrier from given prefix
# input: prefix: string
# output: carrier: string
def read_item(prefix: Union[str, None] = None):
    return "Hello World!"
