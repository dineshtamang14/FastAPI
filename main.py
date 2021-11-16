from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "hello world"
    }


@app.get("/post")
async def gets_post():
    return {
        "post": "this is your first post"
    }
