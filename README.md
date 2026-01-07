
---

# 📖 My Recipe Book

A Django-based web application that allows authenticated users to **create, view, search, update, and delete recipes**, including image uploads. The app also includes **user registration, login, and logout functionality**.

---

## 🚀 Features

- User Registration & Login (Django Authentication)
- Login-protected Recipe Dashboard
- Add recipes with images
- Search recipes by name
- Update existing recipes
- Delete recipes
- Flash messages for user feedback
- Bootstrap-powered UI

---

## 🛠️ Tech Stack

- Python
- Django
- SQLite (default)
- Bootstrap
- HTML / CSS

---

## 📂 Project Structure

```

my_project/
│
├── home/                # App for authentication & landing pages
├── recipe/              # App for recipe CRUD operations
├── media/               # Uploaded recipe images
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS)
├── manage.py
└── my_project/          # Project settings

````

---

## 🔐 Authentication Flow

- Users must **register** before logging in
- Only logged-in users can:
  - View recipes
  - Add new recipes
  - Update recipes
  - Delete recipes
- Unauthorized users are redirected to the login page

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Kaushal-jain01/Recipe-Book-App.git
cd Recipe-Book-App
````

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 🖼️ Image Uploads

- User-uploaded recipe images are stored in `public/media/recipes/`
- Static assets (CSS, JS) are served from `public/static/`
- `MEDIA_ROOT` and `MEDIA_URL` are configured separately from static files

---

## 🧠 Learning Outcomes

* Django authentication system
* CRUD operations
* File uploads
* Template rendering
* Query filtering & search
* Login-required views

---

## 📌 Future Improvements

* User-specific recipes
* Pagination
* Recipe categories
* Likes & comments
* REST API integration

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

---
