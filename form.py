from fastapi import FastAPI,Form
from typing import Annotated
from pydantic import BaseModel

app=FastAPI()

class FormData(BaseModel):
    username:str
    password:str

@app.post("/logindetails/")
async def logindetails(data:Annotated[FormData,Form()]):
    return data

@app.post("/login/")
async def login(username: Annotated[str,Form()],password: Annotated[str,Form()]):
    return{"username":username}
