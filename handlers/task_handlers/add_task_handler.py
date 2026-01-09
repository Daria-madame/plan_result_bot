import aiosqlite
from aiogram.types import Message

from handlers.task_status import TaskStatus


async def add_task_handler(message: Message) -> None:
    async with aiosqlite.connect("my_database.db") as db:
        plan_id = await (await db.execute(f"Select id from Plan where user_id={message.from_user.id}")).fetchone()
        description = message.text[len("/add_task") + 1 :]
        if not description:
            await message.answer("No description")
            return
        await db.execute(
            "INSERT INTO Task (description, plan_id, status) VALUES (?, ?, ?)",
            (description, plan_id[0], TaskStatus.IN_PROGRESS.value),
        )
        await db.commit()
    await message.answer("Task added!")
