from random import randrange
from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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


@app.get("/posts", status_code=status.HTTP_201_CREATED)
async def gets_post():
    return {"data": my_posts}


@app.get("/posts/{id}")
async def get_post(id: int):
    post = find_post(id)
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"post with id: {id} was not found"}
    return {"post_detail": post}


# post request
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


# delete route
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    index = find_index_id(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    # return {"message": "post was delete successfully"}
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# update route
@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    index = find_index_id(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict

    return {"data": post_dict}



