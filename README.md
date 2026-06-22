# telegram-bot
Telegram bot for users and admin management system
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("TOKEN")
ADMIN = int(os.getenv("ADMIN"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 پیام بده")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    msg = f"""
📩 پیام جدید

🆔 ID: {user.id}
👤 Username: @{user.username}
💬 Message: {update.message.text}
"""

    await context.bot.send_message(chat_id=ADMIN, text=msg)
    await update.message.reply_text("ارسال شد ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()
