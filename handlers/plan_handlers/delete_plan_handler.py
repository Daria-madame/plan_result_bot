import time

from aiogram.types import Message
from sqlalchemy import delete, select

from db.base import Session
from db.plan_orm import PlanORM


async def delete_plan_handler(message: Message) -> None:
    async with Session() as session:
        plan_id = message.text[len("/delete_plan") + 1:]
        if not plan_id.isdigit():
            await message.answer("Failed! Please, write numbers!")
            return
        plan_id = int(plan_id)
        appropriate_request = select(PlanORM).where(PlanORM.id == plan_id)
        result = await session.scalar(appropriate_request)
        if not result:
            await message.answer(f"Plan with {plan_id} doesn`t exist! Try again!")
            return
        stm = delete(PlanORM).where(PlanORM.id == int(message.text[len("/delete_task") + 1:]))
        await session.execute(stm)
        await session.commit()

    await message.answer("Plan successfully deleted!")
