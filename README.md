# 💼 Interview Application Tracker

A Full-Stack Job Application Tracking System built using FastAPI, Streamlit, PostgreSQL, and SQLAlchemy.

This project helps users track job applications, monitor application status, manage interview progress, and store application details in a PostgreSQL database.

---

# 📌 Project Overview

Applying to multiple companies can become difficult to manage.

This application allows users to:

- Add job applications
- View all applications
- Update application details
- Delete applications
- Track application status
- Store data permanently in PostgreSQL
- Visualize applications through Streamlit

---

# 🎯 Problem Statement

When applying to multiple companies, candidates often lose track of:

- Which companies they applied to
- Current application status
- Interview schedules
- Application links
- Notes and feedback

This project solves that problem by providing a centralized dashboard for managing job applications.

---

# 🛠️ Tech Stack

## Backend

- FastAPI
- Pydantic
- SQLAlchemy
- Uvicorn

## Frontend

- Streamlit

## Database

- PostgreSQL
- pgAdmin

## Other Tools

- Git
- GitHub
- Swagger UI

---

# 🏗️ System Architecture

```text
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
SQLAlchemy ORM
        │
        ▼
PostgreSQL Database
```

---

# 📂 Project Structure

```text
Interview-Application-Tracker/

│
├── app.py
├── main1.py
├── database.py
├── models.py
├── schemas.py
├── create_tables.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Database Design

Database Name:

```text
Fastapi
```

Table Name:

```text
applications
```

Columns:

| Column | Data Type |
|----------|----------|
| id | Integer |
| company | String |
| role | String |
| location | String |
| status | String |
| salary | String |
| application_date | Date |
| job_link | String |
| notes | String |

---

# 🚀 Features

## Create Application

Users can create a new job application.

Example:

```json
{
  "id": 1,
  "company": "Google",
  "role": "Data Analyst",
  "location": "Hyderabad",
  "status": "Applied",
  "salary": "8 LPA",
  "application_date": "2026-06-20",
  "job_link": "https://careers.google.com",
  "notes": "Applied through referral"
}
```

---

## Read Applications

Users can view:

- All applications
- Individual application details

---

## Update Application

Users can update:

- Company
- Role
- Location
- Status
- Salary
- Notes

Example:

```text
Applied
↓
Interview Round 1
↓
HR Round
↓
Selected
```

---

## Delete Application

Users can remove unwanted application records.

---

## Application Status Tracking

Supported statuses:

```text
Applied
Shortlisted
Assessment
Interview Round 1
Interview Round 2
HR Round
Selected
Rejected
```

---

# 🔌 FastAPI API Endpoints

## Home

```http
GET /
```

---

## Create Application

```http
POST /applications
```

---

## Get All Applications

```http
GET /applications
```

---

## Get Single Application

```http
GET /applications/{application_id}
```

---

## Update Application

```http
PUT /applications/{application_id}
```

---

## Delete Application

```http
DELETE /applications/{application_id}
```

---

# 🗄️ PostgreSQL Setup

## Install PostgreSQL

Verify installation:

```bash
psql --version
```

---

## Start PostgreSQL

```bash
brew services start postgresql@17
```

---

## Connect to PostgreSQL

```bash
psql -d postgres
```

---

## Create Database

```sql
CREATE DATABASE Fastapi;
```

---

# ⚙️ SQLAlchemy Configuration

database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/Fastapi"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

---

# 🧩 Database Model

models.py

```python
class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    company = Column(String)
    role = Column(String)
    location = Column(String)
    status = Column(String)
    salary = Column(String)
    application_date = Column(Date)
    job_link = Column(String)
    notes = Column(String)
```

---

# 📋 Create Tables

Run:

```bash
python create_tables.py
```

This creates the applications table automatically.

---

# ▶️ Running the Backend

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main1:app --reload
```

API runs at:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Running Streamlit

Run:

```bash
streamlit run app.py
```

Streamlit runs at:

```text
http://localhost:8501
```

---

# 📈 Future Improvements

- User Authentication
- Interview Review Module
- Resume Upload Feature
- Email Notifications
- PostgreSQL Cloud Deployment
- Docker Containerization
- Analytics Dashboard
- Search and Filtering
- Multi-User Support

---

# 🧪 Testing

CRUD operations tested using:

- Swagger UI
- PostgreSQL Queries
- Streamlit Frontend

Verified:

✅ Create

✅ Read

✅ Update

✅ Delete

---

# 💡 Learning Outcomes

Through this project, I learned:

- FastAPI Development
- REST API Design
- CRUD Operations
- PostgreSQL Database Management
- SQLAlchemy ORM
- Streamlit Frontend Development
- API Testing using Swagger
- Git & GitHub Version Control

---

# 👨‍💻 Author

Ravi Kiran Gandupalli

B.Tech CSE (Data Science)

Python | FastAPI | Data Science | Machine Learning

GitHub:
https://github.com/raviguna901

---

# ⭐ Conclusion

This project demonstrates the integration of FastAPI, Streamlit, SQLAlchemy, and PostgreSQL to build a complete full-stack application for tracking job applications and interview progress.

The system provides persistent storage, API-driven architecture, and an interactive user interface, making it suitable for learning modern backend and full-stack development concepts.