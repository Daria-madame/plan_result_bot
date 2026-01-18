from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class PlanORM(Base):
    __tablename__ = "Plan"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer())
    created_at: Mapped[int] = mapped_column()

    def __repr__(self):
        return f" 'id': {self.id}, 'user_id': {self.user_id}, 'created_at': {self.created_at}"
