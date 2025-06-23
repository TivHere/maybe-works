from telegram import Update
from telegram.ext import ContextTypes
from .menu import MAIN_MENU, get_back_menu

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome! Please choose an option:",
        reply_markup=MAIN_MENU
    )

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "option_1":
        await query.edit_message_text(
            text="ℹ️ You selected Option 1.\n\nDetails go here.",
            reply_markup=get_back_menu()
        )
    elif query.data == "option_2":
        await query.edit_message_text(
            text="📊 You selected Option 2.\n\nMore info here.",
            reply_markup=get_back_menu()
        )
    elif query.data == "option_3":
        await query.edit_message_text(
            text="📄 You selected Option 3.\n\nOther details here.",
            reply_markup=get_back_menu()
        )
    elif query.data == "main_menu":
        await query.edit_message_text(
            text="👋 Welcome back! Choose an option:",
            reply_markup=MAIN_MENU
        )
