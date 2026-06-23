import os
import logging
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load env
load_dotenv()

TOKEN = os.getenv("TOKEN")
ADMIN = os.getenv("ADMIN")

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"سلام {user.first_name} 👋\n"
        f"به ربات خوش آمدید."
    )

    # ارسال پیام به ادمین (اختیاری)
    if ADMIN:
        try:
            await context.bot.send_message(
                chat_id=int(ADMIN),
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
