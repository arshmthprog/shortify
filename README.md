# shortify
URL shortening service with custom short links and click tracking built using Django.

Shortify 🔗

A simple URL shortener built with Django.

🚀 Features
Shorten long URLs into compact links
Redirect short links to original URLs
Simple and clean UI using Django templates
🛠 Tech Stack
Django (Backend + Templates)
SQLite (default database)
📦 Installation

Clone the repository:

git clone https://github.com/your-username/shortify.git
cd shortify

Create virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install django

Run migrations:

python manage.py migrate

Start development server:

python manage.py runserver
🌐 Usage

Open your browser and go to:

http://127.0.0.1:8000/
Paste a long URL
Get your shortened link
Use it and get redirected automatically
📁 Project Structure
shortify/
├── core/              # Main app
├── shortify/          # Project settings
├── db.sqlite3
└── manage.py
📌 Notes
This project uses only Django (no external packages)
Built with Django templates (no frontend framework)
Designed for learning and simplicity
📄 License

This project is open-source and free to use.