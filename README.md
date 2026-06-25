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
No accounts. No tracking pixels. No bullshit — just paste, shorten, share.

Built on Django with zero unnecessary dependencies.

---

## Features

| | |
|---|---|
| 🔗 **URL Shortening** | Converts any long URL into a clean short link |
| ⚡ **Instant Redirect** | Sub-millisecond lookups, straight to the destination |
| 🧩 **Template UI** | Server-rendered — no JS framework overhead |
| 🪶 **Lightweight** | Single Django app, SQLite, done |

---

## Stack

```
Backend    →  Python 3.11 + Django 4.x
Database   →  SQLite (zero config)
Frontend   →  Django Templates (HTMl/CSS only)
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
git clone https://github.com/your-username/shortify.git
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

That's it. No magic.

---

## License

MIT — take it, fork it, ship it.
