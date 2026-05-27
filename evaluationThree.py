from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="my_db"
)

cursor = db.cursor()

class User(BaseModel):
    id: str
    name: str
    marks: int

@app.post("/userDetails")
def create_user(user: User):
    query = """
        INSERT INTO userTable (id, name, marks)
        VALUES (%s, %s, %s)
    """

    values = (user.id, user.name, user.marks)

    cursor.execute(query, values)
    db.commit()

    return {
        "message": "Employee created successfully",
        "status_code": 200
    }

@app.get("/userDetails")
def get_users():
    query = "SELECT * FROM userTable"

    cursor.execute(query)

    users = cursor.fetchall()

    return users



@app.put("/userDetails/{user_id}")
def update_employee(user_id: int, user: User):

    cursor.execute(
        "SELECT * FROM userTable WHERE id = %s",
        (user_id,)
    )

    result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")

    query = """
        UPDATE userTable
        SET id=%s, name=%s, marks=%s
        WHERE id=%s
    """

    values = (
        user.id,
        user.name,
        user.marks,
        user_id
    )

    cursor.execute(query, values)
    db.commit()

    return {"message": "Employee updated successfully","Status_code":200}


@app.delete("/userDetails/{user_id}")
def delete_employee(user_id: int):

    cursor.execute(
        "SELECT * FROM userTable WHERE id = %s",
        (user_id,)
    )

    result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")

    query = "DELETE FROM userTable WHERE id = %s"

    cursor.execute(query, (user_id,))
    db.commit()

    return {"message": "Employee deleted successfully","status_code":200}
