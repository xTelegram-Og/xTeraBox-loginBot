import os
import logging
import pathlib
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- Start Command Handler ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = user.first_name if user.first_name else "There"

    msg1 = (
        f"Hey {username},\n"
        f"Welcome To xTera Login\\!\\!\n\n"
        "This Is A Login Bot Designed To Help You Get Access To The *xTera Downloader* Bot In 3 Easy Steps:\n\n"
        "1️⃣ Get The Subscription On\n"
        "👉 @xTera\\_Payment\n\n"
        "2️⃣ Share The Screenshot With\n"
        "👉 @xTeraOG\n\n"
        "3️⃣ Get The Invite Link In Your DM\n"
        "👉 \\@Sit Back \\& Enjoy\\!\n"
    )
    await update.message.reply_text(msg1, parse_mode="MarkdownV2")

    msg2 = (
        "⭐ *SUBSCRIPTION* ⭐\n\n"
        "✨ *₹99 – Basic \\(1 Month\\)*\n\n"
        "🌙 *₹149 – Standard \\(1 Year\\)*\n\n"
        "🔥 *₹199 – Premium \\(Lifetime\\)*\n\n"
    )

    # Absolute path for image
    image_path = pathlib.Path(__file__).parent / "QR_Pay.png"
    with open(image_path, 'rb') as photo:
        await update.message.reply_photo(photo=photo, caption=msg2, parse_mode="MarkdownV2")

    msg3 = (
        "💸 *Payment Instructions*\n\n"
        "Make The Payment Using The UPI ID\\.\n\n"
        "Send The Payment Screenshot To @xTeraBoxOG\\.\n\n"
        "Once Verified, Your Bot Access Link Will Be Delivered Instantly\\! 💖✨\n\n"
        "🛠 *Need Help?*\n\n"
        "For Any Questions Or Issues, Feel Free To Contact: 👉 @xTeraBoxOG"
    )
    await update.message.reply_text(msg3, parse_mode="MarkdownV2")

    keyboard = [
        [InlineKeyboardButton("xTera", url="https://t.me/xTeraOG")],
        [InlineKeyboardButton("xTera Demo", url="https://t.me/xTera_Demo")],
        [InlineKeyboardButton("xTera Links", url="https://t.me/xTera_Links")],
        [InlineKeyboardButton("xTera Payment", url="https://t.me/xTera_Payment")],
        [InlineKeyboardButton("xTera Payment Proofs", url="https://t.me/xTera_Payment_Proof")],
        [InlineKeyboardButton("xTera Chat Group", url="https://t.me/xTera_Chat_Group")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Stay Connected\\! Click Below To Join Our Channels And Groups 👇",
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )

# --- Main Function ---
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    print("Loaded token:", token)  # TEMP DEBUG

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()