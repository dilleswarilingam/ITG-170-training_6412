from fastapi import FastAPI
from test import Item
from student import StudentName
import mysql.connector

app = FastAPI()

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="mydb"
)

cursor=connection.cursor()
@app.get("/products")
def get_products():
    cursor.execute("SELECT * FROM products")
    products=cursor.fetchall()
    return{"products":products}

@app.get("/")
def home():
    return {"message": "FastAPI working"}

@app.get("/about")
def about(skip: int=0,limit: int=10):
    return {"message": "About Page"}

@app.get("/names/{student_name}")
async def get_name(student_name : StudentName):
    if student_name==StudentName.sample:
        return{"Error":"Please enter a valid name "}
    if student_name== StudentName.x:
        return{"name":student_name,"grade":"You got A grade"}
    if student_name==StudentName.y:
        return{"name":student_name,"grade":"You got B grade"}
    return{"name":student_name,"grade":"You got C grade"}

@app.get("/users/{id}")
def get_id(id: int):
    return {"id":id}

@app.post("/items")
def get_items(item:Item):
    return{ "message": "Product created",
        "data": item}
