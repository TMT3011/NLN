from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models.student import Student
from schemas.student import StudentCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@router.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.delete("/students/{id}")
def delete_student(
    id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == id
    ).first()

    db.delete(student)
    db.commit()

    return {"message": "Deleted"}