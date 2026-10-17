from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import random
import os

# Public links
WEBSITE = "https://hamimextra7.netlify.app/"
OWNER = "https://t.me/Hamimextra2007"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    keyboard = [
        [InlineKeyboardButton("🌐 Website", url=WEBSITE)],
        [InlineKeyboardButton("👨‍💻 Owner", url=OWNER)],
        [InlineKeyboardButton("🎮 Dino Game", callback_data="dino")],
        [InlineKeyboardButton("👤 Profile", callback_data="profile")],
        [InlineKeyboardButton("❓ Help", callback_data="help")],
    ]

    await update.effective_message.reply_text(
        f"🤖 Welcome {user.first_name}!\n\n"
        "🔥 Welcome to X-EXTRA BOT\n\n"
        "👇 Select an option below:",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "profile":
        user = query.from_user
        username = f"@{user.username}" if user.username else "No Username"
        await query.message.reply_text(
            "👤 YOUR PROFILE\n\n"
            f"🆔 ID: {user.id}\n"
            f"📛 Name: {user.first_name}\n"
            f"🔗 Username: {username}"
        )

    elif query.data == "help":
        await query.message.reply_text(
            "❓ HELP MENU\n\n"
            "/start - Open Main Menu\n\n"
            "🌐 Website - Visit our website\n"
            "👨‍💻 Owner - Contact the owner\n"
            "🎮 Dino Game - Try the Dino score demo\n"
            "👤 Profile - View your Telegram profile\n\n"
            "✅ Bot is running!"
        )

    elif query.data == "dino":
        result = random.choice([
            "🦖 Jump! +10 Score",
            "🦖 Perfect Jump! +20 Score",
            "🐦 Bird Avoided! +15 Score",
            "🌵 Game Over! Try Again",
        ])
        await query.message.reply_text(
            f"🎮 DINO GAME\n\n{result}\n\n"
            "Play again from the menu! 🎮"
        )


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "Missing BOT_TOKEN. Add it in Render > Environment > Environment Variables."
        )

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("X-EXTRA BOT RUNNING...")
    app.run_polling()


if __name__ == "__main__":
    main()
