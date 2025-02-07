from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.crude import crude
from app.shemas.schemas import Task, TaskCreate, TaskUpdate

router = APIRouter()


@router.post("/tasks/create", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crude.create_task(db=db, task=task)


@router.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crude.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.patch("/tasks/{task_id}/update", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = crude.update_task(db=db, task_id=task_id, task=task)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.get("/tasks", response_model=list[Task])
def list_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return crude.get_tasks(db=db, skip=skip, limit=limit)
