from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str

class Student(StudentCreate):
    id: int

    class Config:
        from_attributes = True