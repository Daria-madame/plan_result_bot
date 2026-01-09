import asyncio
import logging
import sqlite3
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from env import TOKEN, FILE_DB
from handlers.plan_handlers.create_plan_handler import create_plan_handler
from handlers.plan_handlers.delete_plan_handler import delete_plan_handler
from handlers.plan_handlers.update_plan_handler import update_plan_handler
from handlers.start_handler import command_start_handler
from handlers.task_handlers.add_task_handler import add_task_handler
from handlers.task_handlers.change_task_status_handler import change_task_status_handler
from handlers.task_handlers.delete_task_handler import delete_task_handler
from handlers.task_handlers.get_task_status_handler import get_task_status_handler


dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    return await command_start_handler(message)


@dp.message(F.text.startswith("/add_task"))
async def add_task(message: Message):
    return await add_task_handler(message)


@dp.message(F.text.startswith("/change_task_status"))
async def change_task(message: Message):
    return await change_task_status_handler(message)


@dp.message(F.text.startswith("/delete_task"))
async def delete_task(message: Message):
    return await delete_task_handler(message)


@dp.message(F.text.startswith("/get_task_status"))
async def get_task_status(message: Message):
    return await get_task_status_handler(message)


@dp.message(F.text.startswith("/create_plan"))
async def create_plan(message: Message):
    return await create_plan_handler(message)


@dp.message(F.text.startswith("/delete_plan"))
async def delete_plan(message: Message):
    return await delete_plan_handler(message)


@dp.message(F.text.startswith("/update_plan"))
async def update_plan(message: Message):
    return await update_plan_handler(message)


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":

    connection = sqlite3.connect(FILE_DB)
    cursor = connection.cursor()

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Plan(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    created_at TIMESTAMP
    )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Task(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description INTEGER NOT NULL,
        plan_id INTEGER,
        status VARCHAR CHECK(status IN ('To do', 'In progress', 'Completed')),
        FOREIGN KEY(plan_id) REFERENCES Plan(id)
        )
        """
    )

    connection.commit()
    connection.close()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
