from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.crude import crude
from app.shemas.schemas import TaskCreate, Task, TaskUpdate

router = APIRouter(prefix="/tasks")


@router.post("/create", response_model=Task)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_session)):
    return await crude.create_task(db=db, task=task)


@router.get("/list", response_model=list[Task])
async def list_tasks(db: AsyncSession = Depends(get_session), skip: int = 0, limit: int = 10):
    return await crude.get_tasks(db=db, skip=skip, limit=limit)


@router.get("/{task_id}", response_model=Task)
async def read_task(task_id: int, db: AsyncSession = Depends(get_session)):
    db_task = await crude.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.patch("/{task_id}/update", response_model=Task)
async def update_task(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_session)):
    db_task = await crude.update_task(db=db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
