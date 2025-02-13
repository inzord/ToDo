from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.models import TaskModel
from app.shemas.schemas import TaskCreate, TaskUpdate


async def create_task(db: AsyncSession, task: TaskCreate):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(TaskModel).filter(TaskModel.id == task_id))
    return result.scalars().first()


async def update_task(db: AsyncSession, task_id: int, task: TaskUpdate):
    db_task = await get_task(db, task_id)
    if db_task:
        for key, value in task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)
        await db.commit()
        await db.refresh(db_task)
    return db_task


async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(TaskModel).offset(skip).limit(limit))
    return result.scalars().all()
