from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8740964769:AAEeF2xJvZ1zKELxixAy4t3evkZ5Om_cqMA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! البوت يعمل بنجاح. 🎉")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
