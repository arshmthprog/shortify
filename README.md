# 🚀 Shortify

> A lightweight URL shortener built with Django

---

## 📌 Overview

Shortify is a minimal web application that converts long URLs into short, shareable links and redirects users to the original destination.
Built with Django using a simple and clean architecture.

---

## ✨ Features

* 🔗 Create short URLs from long links
* ↪️ Instant redirection to original URLs
* 🧩 Simple Django template-based UI
* ⚡ Lightweight and fast

---

## 🧰 Tech Stack

* Python
* Django
* SQLite
* Django Templates

---

## 📁 Project Structure

shortify/
├── core/
├── shortify/
├── db.sqlite3
└── manage.py

---

## ⚙️ Setup & Installation

### 1. Clone the repository

git clone [https://github.com/your-username/shortify.git](https://github.com/your-username/shortify.git)
cd shortify

### 2. Create virtual environment

python -m venv venv
source venv/bin/activate   (Windows: venv\Scripts\activate)

### 3. Install dependencies

pip install django

### 4. Apply migrations

python manage.py migrate

### 5. Run the server

python manage.py runserver

---

## 🌐 Usage

Open in browser:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Then:

* Paste a long URL
* Generate a short link
* Share it

---

## 📄 License

MIT License — free to use
