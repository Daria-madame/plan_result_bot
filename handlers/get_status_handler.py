import datetime

import aiosqlite
from aiogram.types import Message
from black.trans import defaultdict
from sqlalchemy import select

from db.base import Session
from db.plan_orm import PlanORM
from db.task_orm import TaskORM


async def get_status_handler(message: Message) -> None:
    async with Session() as session:
        user_id = message.from_user.id
        plan_query = select(PlanORM).where(PlanORM.user_id == user_id).order_by(PlanORM.created_at)
        plans = (await session.scalars(plan_query)).all()
        task_query = select(TaskORM).where(TaskORM.plan_id.in_([p.id for p in plans]) )
        tasks = (await session.scalars(task_query)).all()


    tasks_map = defaultdict(list)
    for task in tasks:
        tasks_map[task.plan_id].append(task)
    answer = ""

    for plan in plans:
        answer += f"План: {datetime.datetime.fromtimestamp(plan.created_at)}"
        answer += "\n".join(f"{task.status} {task.description}" for task in tasks_map[plan.id] )
        answer += "\n"

    if not answer:
        answer = 'Планов нет'
    await message.answer(answer)