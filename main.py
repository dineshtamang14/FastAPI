from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {
        "message": "hello Peter"
    }


@app.get("/post")
async def gets_post():
    return {
        "post": "this is your first post"
    }

#post request
@app.post("/create_post")
async def create_post(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}
