import re
from aiogram import types
from decimal import Decimal
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
import payment
import request.requests
from commands.keyboards import *
from request.requests import *
from text import texts

router = Router()

class Statedef(StatesGroup):
    waiting_for_text = State()
    waiting_for_text_2 = State()
    waiting_for_text_3 = State()
    waiting_for_text_4 = State()
    waiting_for_text_5 = State()
    waiting_for_text_6 = State()
    waiting_for_text_7 = State()
    waiting_for_email = State()
    waiting_for_amount = State()
    user_pay = State()

def get_text(key1, key2):
    return texts[key1][key2]

@router.message(Command("start"))
async def start(message: Message):
    request.requests.start_create(message.from_user.id, message.from_user.username)
    await message.answer_photo(photo="https://postpic.net/i/8hRQg", caption="🧑‍💻 Добро пожаловать в Ethical Hacker Library 🧑‍💻", reply_markup=start_button())

@router.callback_query(F.data == "back_profile")
async def subs(callback: CallbackQuery):
    data = get_user_profile(callback.from_user.id)
    data2 = get_sub_user(callback.from_user.id)

    new_photo = types.InputMediaPhoto(media="https://postpic.net/i/8hkjC",
                                      caption=f"""➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n👤 Username: {data[3]}\n🔑 id: {data[1]}\n\n💳 Баланс: {data[4]} руб\n\n⏱ Дата регистрации: {data[2]}\n\n👑 Ваши подписки:\n""")

    subscription_levels = [data2[0], data2[1], data2[2], data2[3], data2[4], data2[5]]
    level_names = ["NCrack", "Sqlmap", "MSFConsole", "SearchSploit", "Hydra", "Nmap"]
    level_emojis = ["✅" if level == 1 else "❌" for level in subscription_levels]

    new_photo.caption += "\n".join([f"{name}: {emoji}" for name, emoji in zip(level_names, level_emojis)])
    new_photo.caption += "\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"

    await callback.message.edit_media(media=new_photo)
    await callback.message.edit_reply_markup(reply_markup=profile_button())

@router.callback_query(F.data == "subs")
async def subs(callback: CallbackQuery):
    new_photo = types.InputMediaPhoto(media="https://postpic.net/i/8hkjC",
                                      caption=f"Выберите подписку")

    await callback.message.edit_media(media=new_photo)
    await callback.message.edit_reply_markup(reply_markup=subs_button(callback.from_user.id))

@router.callback_query(F.data == "back")
async def subs(callback: CallbackQuery):
    new_photo = types.InputMediaPhoto(media="https://postpic.net/i/8hRQg",
                                      caption=f"🧑‍💻 Добро пожаловать в Ethical Hacker Library 🧑‍💻")

    await callback.message.edit_media(media=new_photo)
    await callback.message.edit_reply_markup(reply_markup=start_button())



@router.callback_query(F.data == "profile")
async def subs(callback: CallbackQuery):
    data = get_user_profile(callback.from_user.id)
    data2 = get_sub_user(callback.from_user.id)


    new_photo = types.InputMediaPhoto(media="https://postpic.net/i/8hkjC",
                                      caption=f"""➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n👤 Username: {data[3]}\n🔑 id: {data[1]}\n\n💳 Баланс: {data[4]} руб\n\n⏱ Дата регистрации: {data[2]}\n\n👑 Ваши подписки:\n""")


    subscription_levels = [data2[0], data2[1], data2[2], data2[3], data2[4], data2[5]]
    level_names = ["NCrack", "Sqlmap", "MSFConsole", "SearchSploit", "Hydra", "Nmap"]
    level_emojis = ["✅" if level == 1 else "❌" for level in subscription_levels]

    new_photo.caption += "\n".join([f"{name}: {emoji}" for name, emoji in zip(level_names, level_emojis)])
    new_photo.caption += "\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖"

    await callback.message.edit_media(media=new_photo)
    await callback.message.edit_reply_markup(reply_markup=profile_button())

@router.callback_query(F.data == "info")
async def subs(callback: CallbackQuery):
    new_photo = types.InputMediaPhoto(media="https://postpic.net/i/8hkjC",
                                      caption=f"Что такое этичный хакинг и чему вы научитесь\n\nЭтичный хакинг - это как игра в 'поймай меня, если\nсможешь', но с добрыми намерениями. Вместо того,\nчтобы красть данные или взламывать системы во\nвред, этичные хакеры (или 'белые шляпы') помогают\nкомпаниям найти уязвимости в своих системах\nбезопасности. Они имитируют атаки\nзлоумышленников, но с целью их предотвратить. ")

    await callback.message.edit_media(media=new_photo)
    await callback.message.edit_reply_markup(reply_markup=back_button())

@router.callback_query(F.data == "warning")
async def subs(callback: CallbackQuery):
    new_photo = types.InputMediaPhoto(media="https://postpic.net/i/8hkjC",
                                      caption=f"Этичный хакинг и почему это безопастно?\n\n• Договор: Этичные хакеры работают по договору с компаниями, которые хотят улучшить свою безопасность.\n• Прозрачность: Они заранее сообщают о своих действиях, а также о результатах и возможных угрозах.\n• Профессионализм: Этичные хакеры – это квалифицированные специалисты, которые прошли специальную подготовку. Они не стараются навредить, а только помочь.")

    await callback.message.edit_media(media=new_photo)
    await callback.message.edit_reply_markup(reply_markup=back_button())

@router.callback_query(F.data == "pay")
async def pay(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Statedef.waiting_for_email)
    await callback.message.answer("📪 Пожалуйста, введите ваш адрес электронной почты для отправки чека")

@router.message(Statedef.waiting_for_email)
async def process_email(message: types.Message, state: FSMContext):
    email = message.text
    pattern = re.compile(r"^\S+@\S+\.\S+$")

    result = pattern.match(email)

    if result is None:
        await message.answer("Пожалуйста, введите корректный адрес электронной почты.")
        return
    else:
        await state.update_data(email=email)
        await state.set_state(Statedef.waiting_for_amount)
        await message.answer("💳 Пожалуйста, введите сумму пополнения")

@router.message(Statedef.waiting_for_amount)
async def process_amount(message: types.Message, state: FSMContext):
    amount_str = message.text
    try:
        amount = Decimal(amount_str).quantize(Decimal("0.00"))
    except:
        await message.answer("Пожалуйста, введите корректную сумму.")
        return

    await state.update_data(amount=amount)
    data = await state.get_data()

    email = data.get("email")
    amount = data.get("amount")

    url, check_payment = payment.create_oplata(email, amount)

    await message.answer_photo(reply_markup=buy(url, check_payment["id"]), caption="Оплата, (Кнопка Проверить оплату работает 1 раз если уже нажали но забыли оплатить создайте новую оплату)",
                               photo="https://postimg.cc/gnvzrrg1")

    id_pay = check_payment["id"]

    await state.set_state(Statedef.user_pay)

    await state.update_data(id_pay=check_payment["id"])

def check_pay(id):

    otvet = payment.oplata_check(id)

    if otvet == True:
        return True

    else:
        return False

@router.callback_query(F.data == "check_buy")
async def pay(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    id_pay = data.get("id_pay")

    data = await state.get_data()
    amount = data.get("amount")

    is_paid = check_pay(id_pay)

    if is_paid:

        await callback.message.answer(text="Оплата успешно прошла. Деньги зачислены.")
        buy_balance(callback.from_user.id, amount)

    else:

        await callback.message.answer(text="Оплата не прошла. Попробуйте снова.")

for i in ["nmap", "hydra", "searchsploit", "msfconsole", "sqlmap", "ncrack"]:
    @router.callback_query(F.data == f"{i}")
    async def yes_orr_no(callback: CallbackQuery, state: FSMContext):
        if get_program(callback.from_user.id, callback.data)[0] != 0:
            url = get_text("url", callback.data)
            await callback.message.answer(f"Ваша ссылка на обучение {url}")
        else:
            if get_user_profile(callback.from_user.id)[4] >= 500.00:
                await callback.message.answer(text="С баланса спишится 500 рублей", reply_markup=yes_or_no())
                await state.set_state(Statedef.waiting_for_text)
                await state.update_data(programm=callback.data)
            else:
                await callback.message.answer(text="У вас недостаточно средств, пополните баланс в профиле")

@router.callback_query(F.data == "yes")
async def yes(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    programm = data.get("programm")
    if get_program(callback.from_user.id, programm)[0] != 1:
        try:
            update_program(callback.from_user.id, programm)
            up_sub_user(callback.from_user.id, 500.00)
            await callback.message.answer("Спасибо за покупку")
            new_photo = types.InputMediaPhoto(media="https://postimg.cc/jWpsMGXP",
                                              caption=f"Выберите подписку")

            await callback.message.edit_media(media=new_photo)
            await callback.message.edit_reply_markup(reply_markup=subs_button(callback.from_user.id))

        except:
            await callback.message.answer("Ошибка")
    else:
        await callback.message.answer("Вы уже приобрели данную подписку")

@router.callback_query(F.data == "subs_info")
async def subs_info(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(photo="https://postpic.net/i/8hRQg", caption="Выберите подписку и узнайте о ней", reply_markup=subs_button_info())

for i in ["nmap_info", "hydra_info", "searchsploit_info", "msfconsole_info", "sqlmap_info", "ncrack_info"]:
    @router.callback_query(F.data == f"{i}")
    async def get_info(callback: CallbackQuery, state: FSMContext):
        data = callback.data
        new_string = data.replace("_info", "")
        text = get_text("preview", new_string)
        await callback.message.answer(text=text, reply_markup=back_button())


@router.callback_query(F.data == "kali_linux")
async def kali_linux(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(photo="https://postpic.net/i/8hRQg",
                                        caption="Вот ссылка на туториал по установке Kali Linux https://telegra.ph/Ustanovka-Kali-Linux-v-VirtualBox-Poshagovoe-rukovodstvo-11-22",
                                        reply_markup=back_button())

@router.callback_query(F.data == "no")
async def no(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(photo="https://postpic.net/i/8hRQg", caption="🧑‍💻 Добро пожаловать в Ethical Hacker Library 🧑‍💻", reply_markup=start_button())
