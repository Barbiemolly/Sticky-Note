# 🗒️ Sticky Notes - Django CRUD Web App

## 📌 Overview
Sticky Notes is a Django-based CRUD application that allows users to create, view, update, and delete notes efficiently. 

This repository contains both the **functional Django application** and **system architecture documentation** for learning and demonstration purposes.

---

## 🗂️ Repository(Sticky-Note) Structure

```
/
├── sticky_notes/             # Full Django application
│   ├── manage.py
│   ├── requirements.txt
│   ├── sticky_notes/         # Django project settings
│   └── notes/                # Django app
│       ├── templates/
│       ├── tests/
│       └── ...
├── architecture design/      # UML diagrams and design documents
│   ├── use_case_diagram.png
│   ├── sequence_diagram.png
│   ├── class_diagram.png
│   └── CRUD_matrix.pdf
├── README.md                 # Project documentation (you are here)
```

---

## 🔧 Features

- ✅ **Create Notes** – Add new notes with title and content
- 📃 **View Notes** – View all saved notes in a list
- 📝 **Edit Notes** – Update notes with visible timestamps
- ❌ **Delete Notes** – Permanently remove unwanted notes
- 📅 **Timestamps** – Automatically display `created_at` and `updated_at`
- 🧪 **Unit Tests** – Full test suite for core functionalities
- 📊 **Architecture Design** – Includes UML diagrams and a CRUD matrix

---

## 🧰 Tech Stack

| Tool        | Description                          |
|-------------|--------------------------------------|
| Python 3.11 | Programming language                 |
| Django 5.2  | Backend web framework                |
| SQLite3     | Default lightweight database         |
| HTML/CSS    | Frontend templating and styling      |
| unittest    | Python standard unit testing module  |

---

## 🚀 Getting Started

### 1. 🔃 Clone the Repository
```bash
git clone  https://github.com/Barbiemolly/Sticky-Note.git
cd Sticky-Note/sticky_notes
```

### 2. 📦 Create and Activate Virtual Environment
```bash
# Windows (PowerShell or CMD)
python -m venv venv
venv\Scripts\activate
```

### 3. 🛠️ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🗄️ Run Database Migrations
```bash
python manage.py migrate
```

### 5. 🔥 Run the Application
```bash
python manage.py runserver
```

Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✅ Running Unit Tests

This project uses Django's built-in `unittest` module.

```bash
python manage.py test notes.tests
```

✅ Tests cover:
- Creating a note and confirming `created_at` exists  
- Viewing the list of notes  
- Editing a note and confirming `updated_at` is refreshed  
- Deleting a note and verifying removal from the database

---

## 🧠 Academic Documentation

Located in the `architecture design/` folder:
- 📌 Use Case Diagram
- 📌 Sequence Diagram
- 📌 Class Diagram
- 📌 CRUD Matrix

---

## 📎 Author

**Molemo "Khethwa"**  
Junior Software Developer   

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

