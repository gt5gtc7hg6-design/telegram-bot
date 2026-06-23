from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8950384612:AAEgcXxAYUO_345JHNL-eT2DaKfI8vtJV2I"
ADMIN_ID = 1979194248

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        "سلام 👋\nپیامت رو برام بفرست."
    )

    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"کاربر جدید:\nID: {user.id}\nUsername: @{user.username}"
        )
    except:
        pass

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
