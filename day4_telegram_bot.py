# day4_telegram_bot.py

import os
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace with your tokens
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

openai.api_key = OPENAI_API_KEY

def start(update, context):
    update.message.reply_text("Hi! Send me a message and I'll chat with AI.")

def chat(update, context):
    user_text = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )
    reply = response.choices[0].message.content
    update.message.reply_text(reply)

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
