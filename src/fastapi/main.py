from fastapi import FastAPI, HTTPException
from typing import List, Union
from models import User, Gender, Role, PutUser

app = FastAPI()


db_users: List[User] = [
    User(
        id="f2ad109a-6c44-479d-9c0f-7582bf8ecb24",
        first_name="Eric",
        last_name="Levicky",
        gender=Gender.male,
        roles=[Role.student],
    ),  # type: ignore
    User(
        id="f2ad109a-6c44-479d-9c0f-7582bf8ecb23",
        first_name="Alyssa",
        last_name="Levicky",
        gender=Gender.female,
        roles=[Role.student],
    ),  # type: ignore
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def fetch_users():
    return {"users": db_users}


@app.post("/api/v1/users")
async def post_user(user: User):
    db_users.append(user)
    return {"id": user.id}


@app.put("/api/v1/users/{user_id}")
async def put_user(user_id, user: PutUser):
    user_to_update: Union[User, None] = None
    for curr_user in db_users:
        if str(curr_user.id) == user_id:
            user_to_update = curr_user
    if user_to_update is None:
        raise HTTPException(
            status_code=404, detail=f"user with id: {user_id} does not exist"
        )
    if user.first_name is not None:
        user_to_update.first_name = user.first_name
    if user.middle_name is not None:
        user_to_update.middle_name = user.middle_name
    if user.last_name is not None:
        user_to_update.last_name = user.last_name
    if user.gender is not None:
        user_to_update.gender = user.gender
    if user.roles is not None:
        user_to_update.roles = user.roles
    return user_to_update


@app.delete("/api/v1/users/{user_id}")
async def delete_user_by_id(user_id):
    for user in db_users:
        if str(user.id) == user_id:
            db_users.remove(user)
            return
    raise HTTPException(
        status_code=404, detail=f"user with id: {user_id} does not exist"
    )


@app.get("/api/v1/users/{user_id}")
async def fetch_user_by_id(user_id):
    for user in db_users:
        if str(user.id) == user_id:
            return user
    raise HTTPException(
        status_code=404, detail=f"user with id: {user_id} does not exist"
    )
