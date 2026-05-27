from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class UserDetails(BaseModel):
    id: int
    name: str
    salary: float
    designation:str

@app.post("/employees")
async def get_details(user:UserDetails):
    result= (f"Id:{user.id},name:{user.name},salary:{user.salary},designation:{user.designation}")
    return result 
