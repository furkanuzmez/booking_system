# 🏨 Facility - Restaurant Booking System

A **Django + PostgreSQL + Docker** based **Facility Booking System** where users can book conference restaurent and facilities.

---

## 🚀 Features
✅ **User Authentication** (Register/Login/Logout)  
✅ **Book Facilities** (Conference Rooms, Halls)  
✅ **Admin Panel** (Approve & Manage Bookings)  
✅ **PostgreSQL Database**  
✅ **Docker Support** (Easy Setup)  
✅ **Unit Tests** (Booking & Facility Management)  

---

## 🛠️ Requirements

### ✅ **Option 1: Run with Docker (Recommended)**
- **Docker** (Install from [Docker](https://www.docker.com/))
- **Docker Compose**

### ✅ **Option 2: Run Manually (Without Docker)**
- **Python 3.12+**
- **PostgreSQL 15+**
- **Virtual Environment (`venv`)**

---

## 🏗️ Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/booking_system.git
cd booking_system
```

---

### **2️⃣ Setup Environment Variables**
Create a `.env` file from `.env.example`:
```sh
cp .env.example .env
```
Modify `.env` with your database credentials.

📄 **Example `.env` file:**
```env
DATABASE_NAME=booking_system_db
DATABASE_USER=postgres
DATABASE_PASSWORD=yourpassword  # Change this before running
DATABASE_HOST=postgres
DATABASE_PORT=5432
SECRET_KEY=your-django-secret-key  # Change this before running
DEBUG=True
```

---

## 🐳 **Run the Project with Docker (Recommended)**

### **1️⃣ Build & Start Containers**
```sh
docker-compose up --build
```

### **2️⃣ Apply Database Migrations**
```sh
docker-compose exec django python manage.py migrate
```

### **3️⃣ Create a Superuser**
```sh
docker-compose exec django python manage.py createsuperuser
```
Follow the prompts to set up an **admin username & password**.

### **4️⃣ Open the App**
- Web App: **http://127.0.0.1:8000/**  
- Admin Panel: **http://127.0.0.1:8000/admin/**  

---

## ⚡ **Run Manually Without Docker**

### **1️⃣ Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Setup PostgreSQL Database**
Ensure PostgreSQL is running and create a database:
```sh
psql -U postgres
CREATE DATABASE booking_system_db;
```

### **4️⃣ Apply Migrations & Run the Server**
```sh
python manage.py migrate
python manage.py createsuperuser  # Create an admin user
python manage.py runserver
```
Visit: **http://127.0.0.1:8000/** 🚀  

---

## 🛠 Running Unit Tests
Run tests inside Docker:
```sh
docker-compose exec django python manage.py test booking
```
Or without Docker:
```sh
python manage.py test booking
```

---

## 🎯 **Project Structure**
```
booking_system/
│── booking/                      # Django App (Bookings Management)
│   ├── migrations/                # Database Migrations
│   ├── templates/                 # HTML Templates
│   ├── tests/                     # ✅ Unit Tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   ├── test_views.py
│   │   ├── test_forms.py
│   ├── models.py                  # Database Models
│   ├── urls.py                     # App URLs
│   ├── views.py                    # App Views
│   ├── forms.py                    # Django Forms
│
│── booking_system/                 # Django Project Config
│   ├── settings.py                  # Django Settings
│   ├── urls.py                       # Project URLs
│
│── static/                         # Static Files (CSS, JS, Images)
│── media/                          # Uploaded Media Files
│── .env.example                    # ✅ Example Env File (Do Not Commit .env)
│── requirements.txt                 # Python Dependencies
│── manage.py                        # Django Management Script
│── Dockerfile                       # Dockerfile for Django App
│── docker-compose.yml                # Docker Compose Config
│── .gitignore                        # Ignore Unnecessary Files
│── README.md                         # Project Documentation
```

---

## 🔧 **Troubleshooting**

### 1️⃣ **Docker Issues**
**Error:** `postgres_db exited with code 0`  
✅ **Solution:**  
- Ensure no other **PostgreSQL instance** is running.
- Run:
  ```sh
  docker-compose down -v
  docker-compose up --build
  ```

### 2️⃣ **Database Issues**
**Error:** `relation "auth_user" does not exist`  
✅ **Solution:** Run migrations inside Docker:
```sh
docker-compose exec django python manage.py migrate
```

### 3️⃣ **Static Files Not Loading**
**Error:** `Not Found: /static/admin/css/base.css`  
✅ **Solution:** Collect static files:
```sh
docker-compose exec django python manage.py collectstatic --noinput
docker-compose restart django
```

---

## 📜 **License**
This project is open-source and available under the **MIT License**.
```

