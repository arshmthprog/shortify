<div align="center">

```
███████╗██╗  ██╗ ██████╗ ██████╗ ████████╗██╗███████╗██╗   ██╗
██╔════╝██║  ██║██╔═══██╗██╔══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
███████╗███████║██║   ██║██████╔╝   ██║   ██║█████╗   ╚████╔╝ 
╚════██║██╔══██║██║   ██║██╔══██╗   ██║   ██║██╔══╝    ╚██╔╝  
███████║██║  ██║╚██████╔╝██║  ██║   ██║   ██║██║        ██║   
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝        ╚═╝  
```

**Long links die here.**

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-092E20?style=flat-square&logo=django&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-22c55e?style=flat-square)

</div>

---

## What is this?

Shortify takes your ugly, bloated URLs and turns them into something people actually want to click.  
Pure backend logic — no frontend framework, no JS overhead, just Django doing its job.

---

## Features

| | |
|---|---|
| 🔗 **URL Shortening** | Converts any long URL into a clean short link |
| ⚡ **Instant Redirect** | Fast lookups, straight to the destination |
| 🧩 **Template UI** | Server-rendered with Django Templates |
| 🪶 **Lightweight** | Single Django app, SQLite, zero bloat |

---

## Stack

```
Backend    →  Python 3.11 + Django 4.x
Database   →  SQLite
Templating →  Django Templates
```

---

## Project Structure

```
shortify/
├── core/               # URL logic, models, views
│   ├── models.py       # ShortURL model
│   ├── views.py        # Create + redirect views
│   └── urls.py
├── shortify/           # Project config
│   ├── settings.py
│   └── urls.py
├── manage.py
└── db.sqlite3
```

---

## Get It Running

```bash
# 1. Clone
git clone https://github.com/arshmthprog/shortify.git
cd shortify

# 2. Virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Dependencies
pip install django

# 4. Database
python manage.py migrate

# 5. Launch
python manage.py runserver
```

Open `http://127.0.0.1:8000/` — you're live.

---

## How It Works

```
User pastes URL  →  Django generates slug  →  Stored in DB
                                                    ↓
User visits short link  →  Django looks up slug  →  301 Redirect
```

---

## License

MIT — take it, fork it, ship it.
