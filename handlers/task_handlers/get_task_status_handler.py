import aiosqlite
from aiogram.types import Message


async def get_task_status_handler(message: Message) -> None:
    answer = ""
    async with aiosqlite.connect("my_database.db") as db:
        answer = str(await (await db.execute("select * from Plan")).fetchmany())
        answer += str(await (await db.execute("select * from Task")).fetchmany())

    await message.answer(answer)
