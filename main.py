import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6199379696:AAEhwplnFtr71WE_wtWbcV6ebG6eIHBqqqo'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# osnovnoe menu
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Напитки"),
            KeyboardButton(text="Лаваш")
        ],
        [
            KeyboardButton(text="Пицца"),
            KeyboardButton(text="Бургер")
        ],
        [
            KeyboardButton(text="Сладости"), 
        ],
        [
            KeyboardButton(text="Локация"),
            KeyboardButton(text="Наши номера")
        ]
        [
            KeyboardButton("videonote")
        ]
    ],
    resize_keyboard=True

)


napitki_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Coca Cola"),
            KeyboardButton(text="Fanta")
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)




@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello ogrizok apple", reply_markup=menu)




@dp.message_handler(text="Напитки")
async def echo(message: types.Message):
    await message.answer(text="Напитки",reply_markup= napitki_keyboards)

@dp.message_handler(text="Pepsi")
async def echo(message: types.Message):
    await message.answer_photo("https://web.lebazar.uz/resources/product/2023/4/18/medium_1684384551441101020102-00199.png",
        caption="Стоит 15.000 сумов")

@dp.message_handler(text="Coca Cola")
async def echo(message: types.Message):
    await message.answer_photo("https://ru.coca-cola.uz/content/dam/one/uz/ru/product-images/coca-cola-classic.jpg",
        caption="Стоит 15.000 сумов")

@dp.message_handler(text="Fanta")
async def echo(message: types.Message):
    await message.answer_photo("https://sambazar.uz/upload-file/2021/01/17/20136/750x750-3baeea84-3e36-42d2-914d-d274a03ea14f.png",
        caption="Стоит 15.000 сумов")
    
@dp.message_handler(text="Назад")
async def echo(message: types.Message):
    await message.answer(reply_markup=menu )
    

@dp.message_handler(text="Локация")
async def echo(message: types.Message):
    await message.answer_location(57.718482167758225, 46.583746947475596 )

@dp.message_handler(text="Наши номера")
async def echo(message: types.Message):
    await message.answer_contact(phone_number="8 800 200 23 16",first_name="oleg")


@dp.message_handler(text="videonote")
async def echo(message: types.Message):
    await message.answer_video_note()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
