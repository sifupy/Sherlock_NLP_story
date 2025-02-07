# Sherlock Holmes Concept Website

This project is an aesthetic website inspired by Sherlock Holmes. It was created as part of our final project for the computational linguistics module and it includes features like topic modeling (available only in the local version).

## 🚀 Live Demo
https://sherlocknlp.vercel.app

## 📦 Repository
(https://github.com/sifupy/Sherlock_NLP_story/)

## 🖥️ Setup Instructions

### 1️⃣ Prerequisites
- **Python** 
- **Git**

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/sifupy/Sherlock_NLP_story
cd sherlock
```

### 3️⃣ Setup (Django with Tailwind)
1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Tailwind CSS:
   ```bash
   python manage.py tailwind install
   ```
4. Build Tailwind CSS:
   ```bash
   python manage.py tailwind build
   ```
5. Run the server:
   ```bash
   python manage.py runserver
   ```

### 4️⃣ Access the Website
- **Local App:** [http://localhost:8000](http://localhost:8000)

## 📝 Notes
- The **topic modeling page** is only available in the local version due to deployment issues.
- No database setup is required.
- If you face any problems, feel free to reach out.

Enjoy exploring the Sherlock Holmes universe! 🕵️‍♂️

