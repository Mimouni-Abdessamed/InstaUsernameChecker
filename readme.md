# 🔍 Instagram Username Checker Bot  

This Python script uses **Selenium** and **undetected_chromedriver** to check the availability of Instagram usernames automatically. It also supports **session saving** to avoid repeated logins.  

## 🚀 Features  
✔️ **Login Automation** – Secure login with user input (no hardcoded credentials).  
✔️ **Session Management** – Saves cookies to avoid re-login.  
✔️ **Custom Username Length** – Generates usernames of any length (3-30).  
✔️ **Human-like Typing & Delays** – Mimics real user behavior.  
✔️ **Avoids Consecutive Special Characters** – Ensures valid usernames.  

## 📥 Installation  

### 1️⃣ Install Dependencies  
```bash
pip install undetected-chromedriver selenium
```

### 2️⃣ Download ChromeDriver  
Ensure **Google Chrome** is installed and download the **matching** [ChromeDriver](https://chromedriver.chromium.org/downloads).  

### 3️⃣ Run the Script  
```bash
python script.py
```

## 🔑 How to Use  
1️⃣ Run the script.  
2️⃣ Enter your **Instagram username & password**.  
3️⃣ Choose a **username length (3-30 characters)**.  
4️⃣ The script will check username availability.  

Available usernames are **saved in `available_usernames.txt`**.  

## ⚠️ Notes  
- The script **mimics human behavior** to avoid bot detection.  
- If **Instagram asks for CAPTCHA**, solve it manually.  
- Avoid **checking too many usernames too quickly** to prevent account restrictions.  

## 🛠 Files to Upload to GitHub  
- `script.py` (your main script)  
- `README.md` (this file)  
- `.gitignore` (optional: to exclude logs, cache, or unnecessary files)  
- `requirements.txt` (list of dependencies for easy installation)  

To generate `requirements.txt`:  
```bash
pip freeze > requirements.txt
```

Now you're ready to **push to GitHub**! 🚀
