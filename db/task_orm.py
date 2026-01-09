from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class TaskORM(Base):
    __tablename__ = "Task"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String())
    status: Mapped[str] = mapped_column(String())
    plan_id: Mapped[int] = mapped_column(ForeignKey("Plan.id"))
