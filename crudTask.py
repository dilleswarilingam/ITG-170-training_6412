from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Dict, Optional

app = FastAPI()



class Student(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    age: int = Field(ge=18, le=60)
    course: str

db: Dict[int, Student] = {}


@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):

    if student_id in db:
        raise HTTPException(status_code=400, detail="Student already exists")

    db[student_id] = student

    return {
        "message": "Student created successfully",
        "data": student
    }


@app.get("/students/{student_id}")
def get_student(student_id: int,details: Optional[bool] = Query(False)):

    student = db.get(student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if details:
        return {
            "student_id": student_id,
            "student_data": student
        }

    return {"name": student.name}


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")

    db[student_id] = updated_student

    return {
        "message": "Student updated successfully",
        "data": updated_student
    }


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in db:
        raise HTTPException(status_code=404, detail="Student not found")

    del db[student_id]

    return {
        "message": "Student deleted successfully"
    }