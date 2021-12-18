from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {
        "About Me": [
            {
                "name": "Dinesh Tamang",
                "age": 21,
                "college": "Dilkap college of Engineering",
                "Branch": "T.E. Comps",
                "GitHub": "https://bit.ly/30C80AA",
                "LinkedIn": "https://bit.ly/3p8QkpW",
                "check my work": "https://dineshtamang.netlify.app",
                "skills": ["Linux", "Reactjs", "Nextjs", "Python",
                           "MongoDB", "PostgreSQL", "Tailwindcss", "C++", "AWS Solution Architect"]
            }
        ]
    }

# Test

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "title of post 2", "content": "content of post 2", "id": 2}]
#
#
# def find_post(id):
#     for p in my_posts:
#         if p.get('id') == id:
#             return p
#
#
# def find_index_id(id):
#     for i, p in enumerate(my_posts):
#         if p.get('id') == id:
#             return i

# @app.get("/sql")
# def test(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"status": posts}
