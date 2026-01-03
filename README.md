# Employee-Management Flask Application

## 🔗 Live Demo
https://employee-management-4jxl.onrender.com

---

## Project Title
Employee-Management Application

---

## Problem Statement
Many beginner projects remain limited to local environments and lack real-world deployment experience.  
This project addresses that gap by implementing a complete backend workflow — from development to cloud deployment — including authentication, database integration, and production debugging.

---

## 📌 Table of Contents
- [Project Title](#project-title)
- [Problem Statement](#problem-statement)
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Database](#database)
- [Tools and Technologies](#tools-and-technologies)
- [Project Structure](#project-structure)
- [Methods / Approach](#methods--approach)
- [Key Insights](#key-insights)
- [Key Features](#key-features)
- [Output](#output)
- [Result](#result)
- [What I Learned](#what-i-learned)
- [How to Run This Project](#how-to-run-this-project)
- [Deplyment](#deployment)
- [Screenshots](#screenshots)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Author](#author)

---

## Overview
The Employee Management Flask Application is a **production-deployed web application** built using Flask and PostgreSQL.  
It supports **user authentication**, **employee CRUD operations**, and demonstrates real-world backend development practices including cloud deployment, environment-based configuration, and session management.

The application is deployed on **Render** and is suitable for showcasing backend and full-stack fundamentals to recruiters.

---


## Database
- **PostgreSQL (Production)**
- Hosted on **Render**
- Connected securely using environment variables

The database stores:
- User accounts (authentication)
- Employee records (CRUD operations)

---

## Tools and Technologies
- **Programming Language:** Python  
- **Framework:** Flask  
- **Database:** PostgreSQL  
- **ORM:** SQLAlchemy  
- **Authentication:** Flask-Login  
- **Frontend:** HTML, CSS  
- **Deployment Platform:** Render  
- **Version Control:** Git & GitHub  

---

## Project Structure

```
Employee-Management-Flask-Application/
│
├── .venv/                  # Virtual environment
├── __pycache__/            # Python cache files
│
├── main.py                 # Application entry point
├── models.py               # Database models / business logic
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore file
│
├── templates/              # HTML templates (Jinja2)
│   ├── emp.html
│   ├── login.html
│   └── register.html
│
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   ├── favicon.png
│   └── download.jpg
│
└── downloads/              # Optional downloaded files
```
---

## How to Run This Project

### 1. Clone the Repository
```bash
git clone https://github.com/vruthvik-chinthoju/employee_management-python-flask-mysql.git
````

### 2. Navigate to the Project Folder

```bash
cd employee_management-python-flask-mysql
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

**Windows**

```bash
set FLASK_APP=main.py
set FLASK_DEBUG=1
flask run
```

**Mac / Linux**

```bash
export FLASK_APP=main.py
export FLASK_DEBUG=1
flask run
```

### 7. Open in Browser

```
http://127.0.0.1:5000
```

---
## Methods / Approach
- Backend routing and request handling using Flask
- Modular Python files for maintainability
- Template rendering using Jinja2
- Static file management for UI styling
- Clean and scalable project structure
- Git-based version control workflow

---

## Key Features
- User Registration and Login
- Session-based authentication
- Add, view, and delete employees
- Secure database connection using environment variables
- Cloud deployment with Render
- Responsive UI (mobile-friendly improvements in progress)

---

## Key Insights
- Understanding Flask’s request–response lifecycle
- Separation of frontend and backend concerns
- Importance of clean and scalable project structure
- Practical usage of Git and GitHub in real projects
- Backend development best practices

---

## Output
- A fully functional Flask web application
- Clean backend and frontend integration
- Well-structured project suitable for interviews and portfolios

---

## Result

The application successfully demonstrates:
-Backend development using Flask
-Authentication and session handling
-PostgreSQL integration
-Real-world deployment and debugging
-Clean and scalable project structure

---

## What I Learned 

-Differences between local and cloud environments
-Importance of environment variables in production
-Database connectivity issues and solutions
-Session persistence and security handling
-CI/CD-style auto-deployment using Render

---

## Conclusion 

This project demonstrates strong fundamentals of Flask backend development, clean code organization, and real-world application structure. It reflects practical skills required for entry-level backend and full-stack development roles.

---

## Future Work

Role-based access (Admin/User)
Search and filter functionality
Pagination for large datasets
REST API version of the application
UI enhancement using a modern CSS framework

---

## Deployment

The application is deployed on Render with:
Managed PostgreSQL database
Environment variables (DATABASE_URL, SECRET_KEY)
Auto-deployment from GitHub
Production-ready configuration

---

## Screenshots

### Login Page
![Login Page](screenshots/Login.png)

### Register Page
![Register Page](screenshots/Register.png)

### Dashboard
![Dashboard](screenshots/Dashboard.png)

## Update
![Update](screenshots/Update.png)

### Mobile View Register
![Mobile View Register](screenshots/Mobile-View-Register.jpg)

### Mobile View Login
![Mobile View Login](screenshots/Mobile-View-Login.jpg)

### Mobile View Dashboard
![Mobile View Dashboard](screenshots/Mobile-View-Dashboard.jpg)

### Mobile View Employee
![Mobile View Employee](screenshots/Mobile-View-Employee.jpg)

### Mobile View Update
![Mobile View Update](screenshots/Mobile-View-Update.jpg)

----

## Author 

**Name:** Chinthoju Vruthvik  
**Contact:** 8919721525  
**LinkedIn:** [Chinthoju Vruthvik](https://www.linkedin.com/in/chinthoju-vruthvik-83754b320)

---
