import os
import telebot
import threading
from dotenv import load_dotenv
from twitter import start_reply_bot

# Load environment variables
load_dotenv()

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Initialize Telegram Bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "👋 Welcome! Your Twitter auto-reply bot is ready.\nUse /start_reply to begin auto-replies.")

@bot.message_handler(commands=['start_reply'])
def start_reply(message):
    bot.send_message(message.chat.id, "🚀 Bot is now auto-replying to GM/GN tweets!")
    threading.Thread(target=start_reply_bot).start()

bot.polling()
