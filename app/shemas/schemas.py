from pydantic import BaseModel
from datetime import date


class TaskBase(BaseModel):
    created_at: date
    updated_at: date
    datetime_to_do: date
    task_info: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(TaskBase):
    datetime_to_do: date | None = None
    task_info: str | None = None
    created_at: date | None = None
    updated_at: date | None = None


class Task(TaskBase):
    id: int

    class Config:
        from_attributes = True
