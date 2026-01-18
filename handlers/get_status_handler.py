import aiosqlite
from aiogram.types import Message
from sqlalchemy import select

from db.base import Session
from db.plan_orm import PlanORM


async def get_status_handler(message: Message) -> None:
    async with Session() as session:
        user_id = message.from_user.id
        appropriate_request = select(PlanORM).where(PlanORM.user_id == user_id)
        plans = await session.scalars(appropriate_request)
    await message.answer(plans)