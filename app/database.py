from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:dinesh1997@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi",
#                                 user="postgres", password="dinesh1997", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("database connection established successfully")
#         break
#     except Exception as error:
#         print("Database connection error")
#         print("Error: ", error)
#         time.sleep(2)
