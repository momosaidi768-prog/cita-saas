from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

from core.payments import create_checkout

TOKEN = "8202293986:AAFEmxYfIbVn6q27j0ibvEOElQF4Y68VPzQ"


# 🚀 start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to SaaS Bot\n\nUse /buy to get VIP"
    )


# 💳 buy
async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id

    url = create_checkout(user_id)

    keyboard = [
        [InlineKeyboardButton("💳 ادفع 9.99€", url=url)]
    ]

    await update.message.reply_text(
        "💳 الدفع الآمن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# ▶️ app
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("buy", buy))

print("🚀 Bot running...")
app.run_polling()
