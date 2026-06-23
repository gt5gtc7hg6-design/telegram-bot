from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8950384612:AAGDrVCuKdIyaKic0rBz9bkzD2-XgwimEDg"
ADMIN_ID = 1979194248 # آیدی عددی خودت

# ذخیره موقت آخرین پیام‌ها (برای reply)
last_users = {}

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "در حال ارسال پیام ناشناس هستی.\n"
        "پیام خودتو بنویس و ارسال کن."
    )

# دریافت پیام کاربران
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        text = update.message.text

        # ذخیره کاربر برای reply
        last_users[user.id] = user.id

        # ارسال برای ادمین
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=(
                "📩 پیام ناشناس جدید\n\n"
                f"👤 ID: {user.id}\n"
                f"👤 Username: @{user.username}\n"
                f"💬 Message: {text}\n\n"
                f"➡️ برای جواب دادن: /reply {user.id} پیام"
            )
        )

        await update.message.reply_text("پیام شما ارسال شد ✅")

    except Exception as e:
        await update.message.reply_text("خطا در ارسال پیام ❌")

# reply از طرف ادمین
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message.from_user.id != ADMIN_ID:
            return

        target_id = int(context.args[0])
        msg = " ".join(context.args[1:])

        await context.bot.send_message(
            chat_id=target_id,
            text=f"📩 پاسخ ناشناس:\n\n{msg}"
        )

        await update.message.reply_text("ارسال شد ✅")

    except:
        await update.message.reply_text("فرمت اشتباهه:\n/reply user_id message")

# اجرای ربات
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("reply", reply))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()
