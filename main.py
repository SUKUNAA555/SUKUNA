from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Welcome message
    welcome_message = "Welcome to our bot! We're excited to have you here. Click the button below to share your contact details."

    # Custom keyboard with "Click Me" button
    keyboard = [[KeyboardButton(text="Click Me", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    # Send welcome message with keyboard
    await update.message.reply_text(text=welcome_message, reply_markup=reply_markup)

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = Application.builder().token("7270437364:AAHRP3WHVS2kpBX5tpBXPgUtMt4rzABuuNA").build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", https://t.me/+E376k1R35Xk3ZjA1))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
