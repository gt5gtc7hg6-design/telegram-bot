import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8950384612:AAEgcXxAYUO_345JHNL-eT2DaKfI8vtJV2I"

# ---- Web server برای Render ----
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

# ---- Telegram bot ----
async def start(update, context):
    await update.message.reply_text("سلام 👋 ربات فعاله")

def main():
    threading.Thread(target=run_server, daemon=True).start()

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.run_polling()

if __name__ == "__main__":
    main()
