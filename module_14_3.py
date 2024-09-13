from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = None
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
rkb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")],
                                    [KeyboardButton(text="Купить")]], resize_keyboard=True)
ilkb = InlineKeyboardMarkup()
il_button_1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
il_button_2 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
ilkb.row(il_button_1, il_button_2)
catalog_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Product1", callback_data="product_buying"),
     InlineKeyboardButton(text="Product2", callback_data="product_buying"),
     InlineKeyboardButton(text="Product3", callback_data="product_buying"),
     InlineKeyboardButton(text="Product4", callback_data="product_buying")]
])

Products = ("Протеин", "Креатин", "BCAA", "Гейнер")
Discription = (
    "Протеин используется в качестве добавки к основной пище и может быть полезен для поддержания "
    "жизненного тонуса организма.",

    "Биологически активная добавка к пище, чистый, микронизированый креатин моногидрат, который является добавкой с "
    "самой большой доказательной базой научных исследований в "
    "области роста мышц, увеличения силы и выносливости атлета.",

    "BCAA - одни из самых важных аминокислот для строительства и ремонта мышц, что делает данный продукт идеальным "
    "спортивным питанием для набора мышечной массы и увеличения выносливости.",

    "Мультикомпонентный гейнер для роста мышц и силовых показателей. Комплекс включает все необходимые вещества, "
    "которые нужны для увеличения качественной мышечной массы и полного "
    "восстановления мускулатуры после физических нагрузок.")


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['Start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=rkb)


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    for i in range(4):
        with open(f"Images/{i+1}.png", "rb") as img:
            await message.answer_photo(img, f'Название: {Products[i]} \n'
                                            f'Описание: {Discription[i]} \nЦена: {(i+1)*100}')
    await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")

@dp.callback_query_handler(text='formulas')
async def get_formula(call):
    await call.message.answer('10 x вес(кг) + 6,25 x рост(см) - 5 x возраст(г)')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=ilkb)


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_weight(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма колорий: "
                         f"{10*float(data['weight'])+6.25*float(data['growth'])-5*float(data['age'])}")
    await state.finish()


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Информация о боте')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
