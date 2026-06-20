🎓 Student Management API using FastAPI

A simple CRUD (Create, Read, Update, Delete) REST API built with FastAPI and Pydantic for managing student records.

🚀 Features

* View all students
* Get student details by ID
* Get unique course names
* Get unique student names
* Get unique student locations
* Add new students
* Update existing student records
* Delete students by ID
* Delete students by Name
* Delete students by Course

🛠️ Tech Stack

* Python 3.12+
* FastAPI
* Pydantic
* Uvicorn

📂 Project Structure

student-management-api/
│
├── main.py
├── requirements.txt
└── README.md

📦 Installation

1. Clone the Repository

git clone https://github.com/raviguna901/FastAPI-Learning.git
cd student-management-api

2. Create Virtual Environment

python -m venv venv

3. Activate Virtual Environment

Windows

venv\Scripts\activate

macOS/Linux

source venv/bin/activate

4. Install Dependencies

pip install fastapi uvicorn

▶️ Run the Application

uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000

📖 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

📌 Available Endpoints

Home

Method	Endpoint	Description
GET	/	Welcome Message

Students

Method	Endpoint	Description
GET	/stud	Get all students
GET	/sid/{id}	Get student by ID
POST	/students_data	Add student
PUT	/students_data	Update student
DELETE	/students_data/id/{id}	Delete student by ID
DELETE	/students_data/name/{name}	Delete student by Name
DELETE	/students_data/course/{course}	Delete students by Course

Utility Endpoints

Method	Endpoint	Description
GET	/courses	Get all unique courses
GET	/names	Get all unique names
GET	/places	Get all unique places

📄 Student Schema

{
  "id": 1,
  "name": "Ravi",
  "place": "AP",
  "course": "DS",
  "marks": 98
}

🧪 Example Request

Add Student

POST /students_data

{
  "id": 5,
  "name": "Kiran",
  "place": "HYD",
  "course": "DA",
  "marks": 85
}

🎯 Future Improvements

* PostgreSQL Integration
* SQLAlchemy ORM
* Authentication & Authorization
* Pagination
* Search & Filtering
* Docker Support
* Unit Testing

👨‍💻 Author

Ravi Guna

B.Tech CSE (Data Science)

FastAPI | Python | Data Science Enthusiast