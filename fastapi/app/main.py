from fastapi import FastAPI
from uvicorn import run

import os

app = FastAPI()

DEBUG = os.getenv("DEBUG")
LOG_LEVEL = os.getenv("LOG_LEVEL")
PROJECT_NAME = os.getenv("PROJECT_NAME")

if DEBUG is None or LOG_LEVEL is None or PROJECT_NAME is None:
    raise ValueError("Environment variables (DEBUG, LOG_LEVEL, PROJECT_NAME) must be set.")

@app.get("/")
def read_root():
    return {'Hello': "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=8000, reload=True)
