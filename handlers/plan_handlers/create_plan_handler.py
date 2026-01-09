import time

from aiogram.types import Message
from sqlalchemy.dialects.sqlite import insert

from db.base import Session
from db.plan_orm import PlanORM


async def create_plan_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    async with Session() as session:
        stm = insert(PlanORM).values([{"user_id": message.from_user.id, "created_at": int(time.time())}])
        await session.execute(stm)
        await session.commit()

    await message.answer("Plan successfully created!")
