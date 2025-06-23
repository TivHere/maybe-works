from telegram import InlineKeyboardButton, InlineKeyboardMarkup

MAIN_MENU = InlineKeyboardMarkup([
    [InlineKeyboardButton("📄 Option 1", callback_data="option_1")],
    [InlineKeyboardButton("📊 Option 2", callback_data="option_2")],
    [InlineKeyboardButton("ℹ️ Option 3", callback_data="option_3")]
])

def get_back_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="main_menu")]
    ])
