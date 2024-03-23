from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InputFile
import logging
from datetime import datetime, timezone, timedelta
import schedule
import asyncio

API_TOKEN = '6906717566:AAE1zCYjMqxJZ5WrlaGcpupwqHvw5pdMvvk'

# Initialize bot and dispatcher
bott = Bot(token=API_TOKEN)
dpp = Dispatcher(bott)

# Configure logging
logging.basicConfig(level=logging.INFO)

KIEV = timezone(timedelta(hours=3))  # Киевское время


@dpp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_full_name = message.from_user.full_name
    logging.info(f'{message.from_user.id} {user_full_name} {datetime.now().astimezone(KIEV)}')

    button1 = KeyboardButton('⧼|Повний розклад|⧽')
    button2 = KeyboardButton('⧼|Розклад на сьогодні|⧽')
    button3 = KeyboardButton('⧼|Все для КР\ПР|⧽')
    greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).row(button1, button2, button3)

    await message.reply(f"Привіт, {user_full_name}!", reply_markup=greet_kb)


@dpp.message_handler(content_types='text')
async def new_message(message: types.Message):
    if message.text == '⧼|Повний розклад|⧽':
        photo = InputFile('Rozkl/povnirozklad.png')
        await bott.send_photo(chat_id=message.chat.id, photo=photo)
    elif message.text == '⧼|Розклад на сьогодні|⧽':
        current_weekday = datetime.now().astimezone(KIEV).weekday()

        if current_weekday == 0:
            photo = InputFile('Rozkl/rozklad_pon.png')
        elif current_weekday == 1:
            photo = InputFile('Rozkl/rozklad_viv.png')
        elif current_weekday == 2:
            photo = InputFile('Rozkl/rozklad_ser.png')
        elif current_weekday == 3:
            photo = InputFile('Rozkl/rozklad_chet.png')
        elif current_weekday == 4:
            photo = InputFile('Rozkl/rozklad_pyat.png')
        else:
            await message.reply(f"{message.from_user.first_name}, так.. Сьгоднi вихiдний.")
            return

        await bott.send_photo(chat_id=message.chat.id, photo=photo)
    elif message.text == '⧼|Все для КР\ПР|⧽':
        site_link = 'https://drive.google.com/file/d/1ZAde7TVeELqglsokTz7_SsQHldohZkuH/view'  # Здесь вы можете указать ваше предопределенное посилання
        await message.reply(f"Штампи: {site_link}")



if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dpp, skip_updates=True)
def determine_week_color():
    start_date = datetime(2023, 10, 1)
    current_date = datetime.now()
    weeks_passed = (current_date - start_date).days // 7

    if weeks_passed % 2 == 0:
        return "yel"
    else:
        return "blu"

"""def determine_week_color():
    start_date = datetime(2023, 10, 4)
    current_date = datetime.now()
    weeks_passed = (current_date - start_date).days // 7

    return "yel" if weeks_passed % 2 == 0 else "blu"


yelblu = input("Сегодня синий день или жёлтый? (yel/blu)\n")"""


async def main():
    TOKEN = "6611731503:AAE3Etgct7VhrDcIi6ZAwaC7-ym_8gMqM74"
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot)



TOKEN = "6906717566:AAE1zCYjMqxJZ5WrlaGcpupwqHvw5pdMvvk"
yelblu = determine_week_color()
GROUP_CHAT_ID = "719562540"
GROUP_CHAT_ID2 = "-1001935371745"
main_id = "719562540"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def himia(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, Хімія.\n⧼|Предмет ✢ Хімія.\n⧼|Учитель ✢ Солокова "
                           "Ольга Миколаївна.\n⧼|Посилання ✢ "
                           "https://meet.google.com/qvu-utzd-fhh\n≿━━━━━━━━━━━━━━━━━━━╾")


async def zaruba(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Так, Зарубіжна література.\n⧼|Предмет ✢ Зарубіжна "
                           "література.\n⧼|Учитель  ✢ Романова Юлія Олексіївна.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/coj-surm-fue\n≿━━━━━━━━━━━━━━━━━━━╾")


async def matematika(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Увага, Математика.\n⧼|Предмет ✢ Математика.\n⧼|Учитель  ✢ Ольга"
                           "Свіріна.\n⧼|Посилання   ✢ https://meet.google.com/xpt-xxip-swz\n≿━━━━━━━━━━━━━━━━━━━╾")


async def fizika(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Так, Фізика|Астрономія.\n⧼|Предмет ✢ "
                           "Фізика|Астрономія.\n⧼|Учитель  ✢ Чепурна Оксана Віталіївна.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/ddq-wquw-rsw\n≿━━━━━━━━━━━━━━━━━━━╾")


async def fizra(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Фіз-Ра. Ура, фiгачимо далі.\n⧼|Предмет ✢ Фіз-ра.\n⧼|Учитель  ✢ "
                           "Галанюк Тетяна Олександрівна.\n⧼|Ссылка   ✢ "
                           "https://meet.google.com/cju-nftk-xaf\n≿━━━━━━━━━━━━━━━━━━━╾")


async def angl(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| He-ya! Іноземна мова.\n⧼|Предмет ✢ Іноземна мова.\n⧼|Учитель ✢ "
                           "Кривоспицька Олена|Смирнова.\n⧼|Посилання - Смирнова ✢ "
                           "https://meet.google.com/fda-pfrm-oms?authuser=0&hs=179\n⧼|Посилання - Кропивницька ✢ "
                           "https://meet.google.com/rtr-qkpr-ngp\n≿━━━━━━━━━━━━━━━━━━━╾")



async def tehno(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Так, Технології.\n⧼|Предмет ✢ Технологія.\n⧼|Учитель  ✢ Мітін "
                           "Вадим.\n⧼|Посилання   ✢ https://meet.google.com/mnr-nyxc-izp\n≿━━━━━━━━━━━━━━━━━━━╾")


async def geografy(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Увага, Географія. \n⧼|Предмет ✢ Географія.\n⧼|Учитель  ✢ "
                           "Завгородня Тетяна Володимирівна.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/bqg-ztzd-nsp\n≿━━━━━━━━━━━━━━━━━━━╾")


async def kultura(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Так, Культурологiя.\n⧼|Предмет ✢ Культурологія.\n⧼|Учитель  ✢ "
                           "Вікторія Степанова.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/jva-yaak-ybv\n≿━━━━━━━━━━━━━━━━━━━╾")


async def istorUk(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повiдомляю, Історія України.\n⧼|Предмет ✢ Історія "
                           "України\n⧼|Учитель  ✢ Пономарева Лариса Валеріївна.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/vzs-ebhe-emt\n≿━━━━━━━━━━━━━━━━━━━╾")


async def ZSU(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повiдомляю, Захист України. \n⧼|Предмет ✢ Захист "
                           "України.\n⧼|Учитель  ✢ Леміш Валерій.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/iai-hwwx-fuo\n≿━━━━━━━━━━━━━━━━━━━╾")


async def biol(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Нагадування, Біологія|Екологія.\n⧼|Предмет ✢ "
                           "Біологія|Екологія.\n⧼|Учитель ✢ Солокова Ольга Миколаївна.\n⧼|Посилання ✢ "
                           "https://meet.google.com/wik-xqzv-duw\n≿━━━━━━━━━━━━━━━━━━━╾")


async def istor(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Увага, Всесвітня історія.\n⧼|Предмет ✢ Всесвітня "
                           "історія.\n⧼|Учитель  ✢ Кучерков Ігор Вікторович.\n⧼|Посилання   ✢ "
                           "https://meet.google.com/fbc-kqhp-gya\n≿━━━━━━━━━━━━━━━━━━━╾")


async def orggodina(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Увага, орг.година.\n⧼|Предмет ✢ Орг Година.\n⧼|Учитель  ✢ "
                           "Пономарева Лариса Валеріївна.\n⧼|Посилання   ✢ Нема. Слiкуйте за "
                           "КН-23\n≿━━━━━━━━━━━━━━━━━━━╾")


async def sebinar(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Консультація по зарубіжній літ-рі.\n⧼|Предмет ✢ "
                           "Зарубіжна.\n⧼|Учитель  ✢ Романова Юлія Олексіївна\n⧼|Telegram ✢ "
                           "julia7300\n≿━━━━━━━━━━━━━━━━━━━╾")


async def arduino(chat_id):
    await bot.send_message(chat_id,

                           '≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Курси по Ардуіно.\n⧼|Предмет ✢ Ардуіно.\n⧼|Учитель ✢ Сергій Брильов '
                           '\n⧼|Посилання ✢ https://meet.google.com/xww-vdvv-udk?authuser=0&hs=179 \n≿━━━━━━━━━━━━━━━━━━━╾')


async def pred(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼|Попрошу проверять ссылку по зарубежной. \n≿━━━━━━━━━━━━━━━━━━━╾")


async def pred2(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼|На сегодня всё. Зарубежной не будет.\n≿━━━━━━━━━━━━━━━━━━━╾")



async def E22(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - E22\n≿━━━━━━━━━━━━━━━━━━━╾")

async def KI23(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - KI23\n≿━━━━━━━━━━━━━━━━━━━╾")

async def ГМ22_2(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - ГМ22-2\n≿━━━━━━━━━━━━━━━━━━━╾")

async def KI22_2(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - KI22-2\n≿━━━━━━━━━━━━━━━━━━━╾")

async def KI22_1(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - KI22-1\n≿━━━━━━━━━━━━━━━━━━━╾")

async def test(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - test\n≿━━━━━━━━━━━━━━━━━━━╾")

async def KН23(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - KН23\n≿━━━━━━━━━━━━━━━━━━━╾")

async def KН22(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Повідомлення, заняття.\n⧼|Группа - KН22\n≿━━━━━━━━━━━━━━━━━━━╾")

async def pred(chat_id):
    await bot.send_message(chat_id,
                           "≿━━━━━━━━━༺♛༻━━━━━━━╾\n⧼| Зараз нема уроку \n≿━━━━━━━━━━━━━━━━━━━╾")


schedule.every().monday.at("08:55").do(lambda: asyncio.create_task(E22(GROUP_CHAT_ID2)))
schedule.every().monday.at("10:35").do(lambda: asyncio.create_task(pred(GROUP_CHAT_ID2)))
schedule.every().monday.at("12:25").do(lambda: asyncio.create_task(KI23(GROUP_CHAT_ID2)))

schedule.every().tuesday.at("08:55").do(lambda: asyncio.create_task(ГМ22_2(GROUP_CHAT_ID2)))
schedule.every().tuesday.at("10:35").do(lambda: asyncio.create_task(KI22_2(GROUP_CHAT_ID2)))
schedule.every().tuesday.at("12:25").do(lambda: asyncio.create_task(pred(GROUP_CHAT_ID2)))
schedule.every().tuesday.at("14:05").do(lambda: asyncio.create_task(pred(GROUP_CHAT_ID2)))

schedule.every().wednesday.at("08:55").do(lambda: asyncio.create_task(KI22_1(GROUP_CHAT_ID2)))
schedule.every().wednesday.at("10:35").do(lambda: asyncio.create_task(pred(GROUP_CHAT_ID2)))
schedule.every().wednesday.at("12:25").do(lambda: asyncio.create_task(KН23(GROUP_CHAT_ID2)))
schedule.every().wednesday.at("14:05").do(lambda: asyncio.create_task(KН22(GROUP_CHAT_ID2)))
schedule.every().thursday.at("08:55").do(lambda: asyncio.create_task(E22(GROUP_CHAT_ID2)))
schedule.every().thursday.at("10:35").do(lambda: asyncio.create_task(pred(GROUP_CHAT_ID2)))
schedule.every().thursday.at("12:25").do(lambda: asyncio.create_task(KI22_1(GROUP_CHAT_ID2)))

schedule.every().friday.at("08:55").do(lambda: asyncio.create_task(KН22(GROUP_CHAT_ID2)))
schedule.every().friday.at("10:35").do(lambda: asyncio.create_task(KI22_2(GROUP_CHAT_ID2)))
schedule.every().friday.at("12:25").do(lambda: asyncio.create_task(ГМ22_2(GROUP_CHAT_ID2)))




# Понедельник
"""schedule.every().monday.at("09:23").do(lambda: asyncio.create_task(pred(GROUP_CHAT_ID)))
schedule.every().monday.at("09:25").do(lambda: asyncio.create_task(zaruba(GROUP_CHAT_ID)))"""
schedule.every().monday.at("10:35").do(lambda: asyncio.create_task(geografy(GROUP_CHAT_ID)))
schedule.every().monday.at("12:25").do(lambda: asyncio.create_task(angl(GROUP_CHAT_ID)))
schedule.every().monday.at("14:05").do(lambda: asyncio.create_task(orggodina(GROUP_CHAT_ID)))
""" """
"""schedule.every().monday.at("15:35").do(lambda: asyncio.create_task(istor(GROUP_CHAT_ID)))"""

# Вторник
schedule.every().tuesday.at("10:35").do(lambda: asyncio.create_task(tehno(GROUP_CHAT_ID)))
schedule.every().tuesday.at("12:25").do(lambda: asyncio.create_task(fizra(GROUP_CHAT_ID)))
schedule.every().tuesday.at("14:05").do(lambda: asyncio.create_task(matematika(GROUP_CHAT_ID)))
schedule.every().tuesday.at("15:35").do(lambda: asyncio.create_task(biol(GROUP_CHAT_ID)))

# Среда
schedule.every().wednesday.at("08:55").do(lambda: asyncio.create_task(istorUk(GROUP_CHAT_ID)))
schedule.every().wednesday.at("10:45").do(lambda: asyncio.create_task(kultura(GROUP_CHAT_ID)))
schedule.every().wednesday.at("12:25").do(lambda: asyncio.create_task(fizika(GROUP_CHAT_ID))) #Поменять потом на 12:25
schedule.every().saturday.at("15:35").do(lambda: asyncio.create_task(ZSU(GROUP_CHAT_ID)))

# Четверг
if yelblu == "yel":
    schedule.every().thursday.at("08:58").do(lambda: asyncio.create_task(kultura(GROUP_CHAT_ID)))
elif yelblu == "blu":
    schedule.every().thursday.at("08:55").do(lambda: asyncio.create_task(fizra(GROUP_CHAT_ID)))
else:
    print("Неверный ввод. Пожалуйста, введите 'yel' или 'blu'.")
schedule.every().thursday.at("10:35").do(lambda: asyncio.create_task(matematika(GROUP_CHAT_ID)))
schedule.every().thursday.at("12:25").do(lambda: asyncio.create_task(himia(GROUP_CHAT_ID)))
""" 
schedule.every().thursday.at("14:05").do(lambda: asyncio.create_task(sebinar(GROUP_CHAT_ID)))
schedule.every().thursday.at("15:35").do(lambda: asyncio.create_task(arduino(GROUP_CHAT_ID)))"""

# Пятница
schedule.every().friday.at("09:14").do(lambda: asyncio.create_task(angl(GROUP_CHAT_ID)))
if yelblu == "yel":
    schedule.every().friday.at("10:35").do(lambda: asyncio.create_task(fizika(GROUP_CHAT_ID)))
elif yelblu == "blu":
    schedule.every().friday.at("10:35").do(lambda: asyncio.create_task(matematika(GROUP_CHAT_ID)))
else:
    print("Неверный ввод. Пожалуйста, введите 'yel' или 'blu'.")
schedule.every().friday.at("12:25").do(lambda: asyncio.create_task(istor(GROUP_CHAT_ID)))

if yelblu == "yel":
    schedule.every().friday.at("13:50").do(lambda: asyncio.create_task(pred2(GROUP_CHAT_ID)))
elif yelblu == "blu":
    schedule.every().friday.at("14:05").do(lambda: asyncio.create_task(zaruba(GROUP_CHAT_ID)))


@dp.message_handler(commands=['go'])
async def go_schedule_cmd(message: types.Message):
    yelblu = determine_week_color()
    chat_id = message.chat.id
    await bot.send_message(chat_id, f"Сейчас {yelblu} неделя. Расписание активировано!")


@dp.message_handler(commands=['getid'])
async def get_id(message: types.Message):
    chat_id = message.chat.id
    await message.reply(f"ID этой группы: {chat_id}")


async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduler())
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
    # ... остальной код

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.create_task(scheduler())
    loop.run_until_complete(loop.create_task(executor.start_polling(dp, skip_updates=True)))

