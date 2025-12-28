from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

telegram_bot_token = "8577059776:AAHOJA4O2TDY3PlA2RTTg6NWwxpYFGa9996623Yc"  # Fake.


async def create_starting_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,  # noqa: F405
):
    """
    Docstring for create_starting_command

    update: Update type of telegram package.
    """
    User = update.effective_user
    await update.message.reply_text(
        f"Hello and welcome to GraveBot! \n {User.first_name and User.last_name or ''}"
    )


# /help function.
async def helpStructure(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    await update.message.reply_text(
        "This is our bot and commads:\n /start, /help and reply some messages."
    )


async def response_handler(message: str):
    if not message:
        return "empty text!"
    user_message = message.lower()
    if "hello" in user_message:
        return "Hi!🖐"
    if "how is it going?" in user_message:
        return "Fine!"
    return "I can't get it!"


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    message = update.message.text
    response = await response_handler(message)
    await update.message.reply_text(response)


if __name__ == "__main__":
    print("bot is running!")
    bot = Application.builder().token(telegram_bot_token).build()
    bot.add_handler(CommandHandler("start", create_starting_command))
    bot.add_handler(CommandHandler("help", helpStructure))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    print("ready")
    bot.run_polling(poll_interval=5)
