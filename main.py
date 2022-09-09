from aiogram import Bot, Dispatcher, executor, types

token = "5778420622:AAHuZ6yCGrYxeQIx3ms6gz3epzQHPCIwP4E"
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler()
async def hello(msg: types.Message):
    await msg.reply(msg.text)

executor.start_polling(dp)