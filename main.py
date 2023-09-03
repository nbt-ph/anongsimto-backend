import psycopg2
from typing import Union
from fastapi import FastAPI
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# database connection
try:
    conn = psycopg2.connect(database=os.environ.get('DB_NAME'),
                            host=os.environ.get('DB_HOST'),
                            user=os.environ.get('DB_USER'),
                            port=os.environ.get('DB_PORT'))
except:
    print("unable to connect to db")

cursor = conn.cursor()

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
def read_item(prefix: Union[str, None] = None, carrier: Union[str, None] = None):
    try:
        current_date = datetime.datetime.now()
        cursor.execute(
            "INSERT INTO prefixes(prefix,carrier,created_at,updated_at) VALUES (%s,%s,%s,%s)", (prefix, carrier, current_date, current_date))
        conn.commit()
    except Exception as e:
        print(e)
        print("error loading prefix data")
    return "OK!"


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
