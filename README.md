# URL_Shortener
A simple yet powerful URL shortener built using **Flask**, **SQLAlchemy**, and **SQLite**. It takes long URLs and shortens them to a unique, easy-to-share link. The app also includes unit tests to ensure stability and correctness.

---

## 🚀 Features

- Shortens any valid URL to a 6-character short URL
- Automatically checks for duplicate original URLs and returns the same short version
- Redirects short URLs to the original destination
- Simple and clean frontend with user-friendly interaction
- Unit testing for models and routes using `pytest`
- Secure environment using `.env` and Flask configuration

---

## 🛠️ Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Frontend**: HTML, CSS (basic styling)
- **Database**: SQLite
- **Testing**: Pytest, Unittest
- **Version Control**: Git & GitHub

---

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/URL_Shortener.git
cd URL_Shortener
```

### 🧪 2. Create and Activate a Virtual Environment

python -m venv venv
venv\Scripts\activate     # On Windows
# source venv/bin/activate  # On macOS/Linux

### 📦 3. Install Dependencies

pip install -r requirements.txt

### 🔐 4. Create .env File

SECRET_KEY=your_flask_secret_key_here

### 🗄️ 5. Run the App

Python run.py

Visit http://127.0.0.1:5000 in your browser.

---

✅ Running Tests

pytest

This will run:

test_routes.py → tests form submission and redirection

test_models.py → tests database model logic





