import asyncio

import chats

import wolframalpha

import threading

import commands

import notifications

import commands

import users

from aiogram import Bot, Dispatcher, executor, types
from config import *

import schedule_func

import groups

from tree import *

groups.update()

commands.load()

schedule_func.load()

client = wolframalpha.Client(BOT_WOLF_TOKEN)
loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    print('Bot started!')

    dp.loop.create_task(notifications.check(time_sleep))
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
