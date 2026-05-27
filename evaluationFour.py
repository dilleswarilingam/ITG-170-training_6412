from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app=FastAPI()
class User(BaseModel):
    name: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):

        if len(value) < 3:
            raise ValueError("Name must contain at least 3 characters")

        return value

@app.post("/users")
def get_user(p:User):
    return (f"name:{p.name}")
