from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = None
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
rkb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")]],
                          resize_keyboard=True)
ilkb = InlineKeyboardMarkup()
il_button_1 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
il_button_2 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
ilkb.row(il_button_1, il_button_2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['Start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=rkb)


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
