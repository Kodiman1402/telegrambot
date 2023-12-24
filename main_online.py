# Telegram Bot in Python
# Erstellt vom Kodiman_Himself (2023)
# Ganz besonderen Dank an Loki1979

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '**************************************'
BOT_USERNAME: Final = '@******************'

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! Danke, dass du mit mir redest! Ich bin der Bot von Kodiman!')


async def hilfe_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bitte schreibe etwas, ich werde antworten! Folgende Befehle sind möglich: /downloads /pw /wizard /apk /hilfe /repo /admin /befehle')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Das ist ein Custom Command!')

async def apk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('https://downloads.kodiman.net/APK/HSK%20Crew%2020.2.0.apk')


async def wizard_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('https://downloads.kodiman.net/Wizards/plugin.program.hsk.crew.wizard.pro-1.1.1.zip')


async def pw_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('XqNkbQ')


async def downloads_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('https://downloads.kodiman.net')


async def befehle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Verfuegbare Befehle - /downloads /pw /wizard /apk /hilfe /repo /admin')


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('@Kodiman')


async def repo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('https://downloads.kodiman.net/Repos20/repository.hsk.crew.repo-1.1.0.zip')


async def video_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('https://www.youtube.com/watch?v=3EL_JQU23JM')


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    # Konversation
    if 'hallo' in processed:
        return 'Na Du?'

    if 'wie geht es dir?' in processed:
        return 'Mir geht es gut!'

    if 'ich mag kodiman' in processed:
        return 'Spenden bitte unter: https://ko-fi.com/kodimanhimself'

    if 'spenden' in processed:
        return 'Spenden bitte unter: https://ko-fi.com/kodimanhimself'

    if 'vavoo' in processed:
        return 'Wir supporten kein Vavoo!!!'

    if 'iptv' in processed:
        return 'Wir supporten keine illegalen IPTV-Listen!!!'

    # Anfragen
    # if 'apk' in processed:
    #   return 'https://downloads.kodiman.net/APK/HSK%20Crew%2020.2.0.apk'

    # return 'Ich verstehe nicht, was du meinst...'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type  # chat oder group
    text: str = update.message.text  # txt zu text korrigiert

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('hilfe', hilfe_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('apk', apk_command))
    app.add_handler(CommandHandler('pw', pw_command))
    app.add_handler(CommandHandler('wizard', wizard_command))
    app.add_handler(CommandHandler('downloads', downloads_command))
    app.add_handler(CommandHandler('befehle', befehle_command))
    app.add_handler(CommandHandler('admin', admin_command))
    app.add_handler(CommandHandler('repo', repo_command))
    app.add_handler(CommandHandler('video', video_command))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)


















    
# Quelle: https://www.youtube.com/watch?v=2TI-tCVhe9k
#         https://youtu.be/vZtm1wuA2yc?si=7NGwix3Zf0WapCjx
#         https://ubuntu.pkgs.org/20.04/ubuntu-universe-amd64/python3-python-telegram-bot_12.4.2-1_all.deb.html
#         https://www.pythonanywhere.com/






