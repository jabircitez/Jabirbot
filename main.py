from telegram import Update
from telegram.ext import *
from utils.config import TOKEN, OWNER_ID
from utils.buttons import main_menu
from utils.db import add_user
from handlers.admin import ban, mute
from handlers.support import forward_to_owner, owner_reply
from handlers.downloader import download_youtube, download_tiktok, download_instagram
from handlers.security import filter_messages

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    add_user(update.effective_user.id)
    await update.message.reply_text(
        "به AFG SUPER BOT خوش آمدید 👑",
        reply_markup=main_menu()
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ban", ban))
    app.add_handler(CommandHandler("mute", mute))
    app.add_handler(CommandHandler("reply", owner_reply))

    app.add_handler(CommandHandler("yt", download_youtube))
    app.add_handler(CommandHandler("tiktok", download_tiktok))
    app.add_handler(CommandHandler("insta", download_instagram))

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_owner))
    app.add_handler(MessageHandler(filters.TEXT, filter_messages))

    print("AFG SUPER BOT RUNNING...")
    app.run_polling()

if __name__ == "__main__":
    main()