# Telegram BOT Project.

### This is a very simple bot for answering some of users messages.

1. Importing Update object from telegram package.

2. Importing Application, CommandHandler, MessageHandler, ContextTypes, filters from telegram.ext.
 - Application: use this object at the end of your code for building your bot.
 - CommandHandler: use it for handling the commad of your bot. (create_starting_command and helpStructure function)
 - MessageHandler: use it for handling messages of your bot. (message_handler function)
 - ContextTypes: using it as default type of telegram.
 - filters: this is very important, because we use logic operator (&) for aparting text and command type fo rour bot.

3. Defining function for start command

4. Defining function for help command

5. Defining two function for handling responses for user

6. And tell the bot to check telegram every 5 seconds.