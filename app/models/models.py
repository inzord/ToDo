from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.core.dependencies import Base


class TaskModel(Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[date] = mapped_column(Date)
    updated_at: Mapped[date] = mapped_column(Date)
    datetime_to_do: Mapped[date] = mapped_column(Date, nullable=False)
    task_info: Mapped[str] = mapped_column(String, nullable=False)
