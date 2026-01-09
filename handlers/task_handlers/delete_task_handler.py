import aiosqlite
from aiogram.types import Message

from handlers.task_status import TaskStatus


async def delete_task_handler(message: Message) -> None:
    async with aiosqlite.connect("my_database.db") as db:
        plan_id = await (await db.execute(f"Select id from Plan where user_id={message.from_user.id}")).fetchone()
        description = message.text[len("/delete_task") + 1 :]
        if not description:
            await message.answer("No description")
            return
        await db.execute("DELETE FROM ... WHERE ...")
        await db.commit()
    await message.answer("Task added!")
