import telebot
import json
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# === CONFIG ===
TELEGRAM_TOKEN = "8437888512:AAEWEB95_T0Cd_wNVok8EDFCP0zgSjrkZKo"  # Replace with your Telegram bot token
CONTROL_FILE_NAME = "bot_control.json"

# === GOOGLE DRIVE AUTH ===
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Use browser-based login on first run
drive = GoogleDrive(gauth)

# === SEARCH OR CREATE CONTROL FILE ===
file_list = drive.ListFile({'q': f"title='{CONTROL_FILE_NAME}' and trashed=false"}).GetList()
if file_list:
    control_file = file_list[0]
else:
    control_file = drive.CreateFile({'title': CONTROL_FILE_NAME})
    control_file.SetContentString(json.dumps({"status": "stopped"}))
    control_file.Upload()

# === TELEGRAM BOT ===
bot = telebot.TeleBot(TELEGRAM_TOKEN)

def update_control_file(status):
    control_file.SetContentString(json.dumps({"status": status}))
    control_file.Upload()

def get_current_status():
    control_file.FetchMetadata()
    content = control_file.GetContentString()
    return json.loads(content).get("status", "unknown")

@bot.message_handler(commands=["start_bot"])
def handle_start(message):
    update_control_file("running")
    bot.reply_to(message, "✅ Bot started!")

@bot.message_handler(commands=["stop_bot"])
def handle_stop(message):
    update_control_file("stopped")
    bot.reply_to(message, "🛑 Bot stopped!")

@bot.message_handler(commands=["status"])
def handle_status(message):
    status = get_current_status()
    bot.reply_to(message, f"📊 Bot status: {status}")

@bot.message_handler(commands=["summary"])
def handle_summary(message):
    bot.reply_to(message, "📈 Summary reporting not implemented yet.")

# === RUN BOT ===
print("Telegram controller bot is now running...")
bot.polling()
