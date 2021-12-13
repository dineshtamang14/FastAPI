from random import randrange
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from sqlalchemy.orm import Session
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi",
                                user="postgres", password="dinesh1997", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection established successfully")
        break
    except Exception as error:
        print("Database connection error")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "title of post 2", "content": "content of post 2", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p.get('id') == id:
            return p


def find_index_id(id):
    for i, p in enumerate(my_posts):
        if p.get('id') == id:
            return i


@app.get("/")
async def root():
    return {
        "message": "hello Peter"
    }


# @app.get("/sql")
# def test(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"status": posts}


