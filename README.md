# 📦Telegram Controller Bot

This is a Python-based Telegram bot hosted on **Replit**. It allows you to control your MT5 Forex trading bot remotely via Telegram by writing commands to a shared Google Drive file. The MT5 bot reads this file and acts on the commands.

---

## 🚀 Features

- ✅ Control your bot via Telegram (`/force_buy`, `/force_sell`, `/start`, `/stop_bot`)
- ✅ Stores commands in Google Drive for MT5 bot to access
- ✅ Works on phone via Telegram
- ✅ Hosted on Replit (no PC required for control)
- ✅ Integrates with MT5 bot on your PC or VPS

---

## 🛠️ Setup Instructions

### 1. Import the Project

You can clone or import this repo directly into Replit:
- Use the **"Import from GitHub"** feature in Replit, or
- Create a new Replit and upload the files

### 2. Required Files

- `telegram_controller.py` → Main bot script  
- `client_secrets.json` → Your Google OAuth credentials (downloaded from Google Cloud)  
- `requirements.txt` → Python packages needed  
- `.replit` → Configuration for Replit to run your code  

### 3. Install Python Packages

Replit usually auto-installs `requirements.txt`. If needed:

```bash
pip install -r requirements.txt
