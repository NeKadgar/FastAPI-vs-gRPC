import time

from fastapi import FastAPI

import databases
import sqlalchemy
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@localhost/db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)

metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(128)),
    sqlalchemy.Column("last_name", sqlalchemy.String(128)),
    sqlalchemy.Column("age", sqlalchemy.Integer),
)
engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()

count = 0
start_time = time.time()


class User(BaseModel):
    first_name: str
    last_name: str
    age: int


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/hello/{name}")
def hello_name(name: str):
    global count, start_time
    count += 1
    if count % 1000 == 0:
        print(f"1000 Hello in {time.time() - start_time}")
        start_time = time.time()
    return {"msg": f"Hello {name}!"}


@app.post("/add_user")
async def create_user(user: User):
    query = users.insert().values(
        first_name=user.first_name,
        last_name=user.last_name,
        age=user.age
    )
    user_id = await database.execute(query)
    global count, start_time
    count += 1
    if count % 100 == 0:
        print(f"100 Users in {time.time() - start_time}")
        start_time = time.time()
    return {"id": user_id}


@app.get("/auth_user")
async def auth_user(user: User):
    query = users.select().where(
        sqlalchemy.and_(
            users.columns.first_name == user.first_name,
            users.columns.last_name == user.last_name,
            users.columns.age == user.age
        )
    )
    selected_user = await database.fetch_one(query)
    global count, start_time
    count += 1
    if count % 1000 == 0:
        print(f"1000 Auth in {time.time() - start_time}")
        start_time = time.time()
    return {"token": f"{selected_user.get('first_name')}_{selected_user.get('last_name')}"}
