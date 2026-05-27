from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import uuid

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    id: str | None = None
    name: str 
    email: str
    age: int 

db: Dict[str, User] = {}



@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    user_id = str(uuid.uuid4())
    user.id = user_id
    db[user_id] = user
    return user


@app.get("/users")
def get_users():
    return list(db.values())




@app.get("/users/{user_id}")
def get_user(user_id: str):
    user = db.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user


@app.put("/users/{user_id}")
def update_user(user_id: str, updated_user: User):
    if user_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    updated_user.id = user_id
    db[user_id] = updated_user
    return updated_user



@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    if user_id not in db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    del db[user_id]
    return None
