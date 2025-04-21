from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = '7980547696:AAGHpHEcvFFac-5hUoFa0yBApZWVTRnBOY8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Bot is running and ready to receive simulated phishing data.")

async def receive_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📩 Received:\n{update.message.text}")

app = ApplicationBuilder().token(7980547696:AAGHpHEcvFFac-5hUoFa0yBApZWVTRnBOY8).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_data))
app.run_polling()
