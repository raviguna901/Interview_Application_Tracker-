from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
@app.get("/")
def welcome():
    return "welcome to build your first profile"

# students_data=[
#     {"id" : 1,"name":"Ravi","place":"AP","course":"DA","marks":78},
#     {"id" : 2,"name":"Guna","place":"AP","course":"DA","marks":90},
#     {"id" : 3,"name":"Praveen","place":"HYD","course":"DS","marks":65},
#     {"id" : 4,"name":"Joy","place":"HYD","course":"DS","marks":56},
#     {"id" : 5,"name":"Mani","place":"AP","course":"DA","marks":98}
# ]

# class Student:
#     def __init__(self,id,name,place,course,marks):
#         self.id=id
#         self.name=name
#         self.place=place
#         self.course=course
#         self.marks=marks


class Students(BaseModel):
    id : int
    name:str
    place:str
    course:str
    marks:int

students_data=[Students(id=1,name="Ravi",place="AP",course="DS",marks=98),
               Students(id=2,name="Guna",place="AP",course="DS",marks=100),
               Students(id=3,name="Praveen",place="HYD",course="DA",marks=44),
               Students(id=4,name="sri",place="HYD",course="DA",marks=66)
]

@app.get("/stud")
def cls_students():
    return students_data

@app.get("/sid/{id}")
def student_by_id(id : int):
    for student in students_data:
        if student.id==id:
            return student
    return "student not found"

@app.get("/courses")
def get_courses():
    courses=set()
    for student in students_data:
        courses.add(student.course)
    if courses:
        return courses
    else:
        return "No courses found"

@app.get("/names")
def get_names():
    names=set()
    for student in students_data:
        names.add(student.name)
    if names:
        return names
    else:
        return "No names found"
    
@app.get("/places")
def get_places():
    places=set()
    for student in students_data:
        places.add(student.place)
    if places:
        return places
    else:
        return "No places found"

@app.post("/students_data")
def add_student( data: Students):

    for student in students_data:
        if student.id == data.id:
            return {"message": "Student already exists"}

    students_data.append(data)

    return {
        "message": "Student added successfully",
        "student": data
    }

@app.put("/students_data")
def update_details(id:int,data:Students):
    for student in range(len(students_data)):
        cur=students_data[student]
        if cur.id==id:
            if data!=students_data[student]:
                students_data[student]=data
                return "Data is updated successfully"
            else:
                return "No new data found"
    else:
        return "Students data not found"


@app.delete("/students_data/id/{id}") 
def delete_data(id:int):
    for student in (students_data):
        if student.id==id:
            students_data.remove(student)
            return "Student removed "
        return "student data doesn't exist"

@app.delete("/students_data/name/{name}")
def name_data(name:str):
    for student in (students_data):

        if student.name.lower()==name.lower():
            students_data.remove(student)
            return "Student Removed"
    return "student data doesn't exist"

@app.delete("/students_data/course/{course}")
def course_name(course:str):
    i=0
    for student in students_data:
        if student.course==course:
            students_data.remove(student)
            i=i+1
    if i:
        return "Course data removed"
    return "No course is available"
