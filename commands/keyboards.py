from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from request.requests import get_sub_user

def start_button():

    start_btn = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Профиль", callback_data="profile")],
       [InlineKeyboardButton(text="Информация о подписках", callback_data="subs_info"), InlineKeyboardButton(text="Как установить Kali Linux", callback_data="kali_linux")],
       [InlineKeyboardButton(text="Подписки", callback_data="subs"), InlineKeyboardButton(text="Тех подержка", url="https://t.me/evilacash_manager")],
       [InlineKeyboardButton(text="Ethical Hacker Info", callback_data="info"), InlineKeyboardButton(text="WARNING", callback_data="warning")],
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return start_btn

def subs_button(tg_id):
  get_subss = get_sub_user(tg_id)

  subs = InlineKeyboardMarkup(inline_keyboard=[
     [InlineKeyboardButton(text=f"Nmap{' ✅' if get_subss[5] else ' ❌'}", callback_data="nmap")],
     [InlineKeyboardButton(text=f"Hydra{' ✅' if get_subss[4] else ' ❌'}", callback_data="hydra")],
     [InlineKeyboardButton(text=f"SearchSploit{' ✅' if get_subss[3] else ' ❌'}", callback_data="searchsploit")],
     [InlineKeyboardButton(text=f"MSFConsole{' ✅' if get_subss[2] else ' ❌'}", callback_data="msfconsole")],
     [InlineKeyboardButton(text=f"Sqlmap{' ✅' if get_subss[1] else ' ❌'}", callback_data="sqlmap")],
     [InlineKeyboardButton(text=f"NCrack{' ✅' if get_subss[0] else ' ❌'}", callback_data="ncrack")],
     [InlineKeyboardButton(text="Меню", callback_data="back")],
  ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню.")

  return subs

def profile_button():

    prof = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Пополнить баланс", callback_data="pay")],
       [InlineKeyboardButton(text="Меню", callback_data="back")],
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return prof

def back_button():

    asd = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Меню", callback_data="back")],
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return asd

def yes_or_no():

    asd = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Да", callback_data="yes"), InlineKeyboardButton(text="Нет", callback_data="no")],
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return asd

def back_profile():

    asd = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text="Профиль", callback_data="back_profile")],
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")
    return asd

def buy(url, id):
    pay = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Ссылка", url=url)],
        [InlineKeyboardButton(text="Проверить оплату", callback_data="check_buy")],
        [InlineKeyboardButton(text="Меню 📖", callback_data="back")]
    ],
                                resize_keyboard=True,
                                input_field_placeholder="Выберите пункт меню.")

    return pay

def subs_button_info():

  subs = InlineKeyboardMarkup(inline_keyboard=[
     [InlineKeyboardButton(text=f"Nmap", callback_data="nmap_info")],
     [InlineKeyboardButton(text=f"Hydra", callback_data="hydra_info")],
     [InlineKeyboardButton(text=f"SearchSploit", callback_data="searchsploit_info")],
     [InlineKeyboardButton(text=f"MSFConsole", callback_data="msfconsole_info")],
     [InlineKeyboardButton(text=f"Sqlmap", callback_data="sqlmap_info")],
     [InlineKeyboardButton(text=f"NCrack", callback_data="ncrack_info")],
     [InlineKeyboardButton(text="Меню", callback_data="back")],
  ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню.")

  return subs