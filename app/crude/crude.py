from typing import List, Type

from sqlalchemy.orm import Session

from app.models.models import TaskModel
from app.shemas.schemas import TaskCreate, TaskUpdate


def create_task(db: Session, task: TaskCreate):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()


def update_task(db: Session, task_id: int, task: TaskUpdate):
    db_task = get_task(db, task_id)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task


def get_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TaskModel).offset(skip).limit(limit).all()
