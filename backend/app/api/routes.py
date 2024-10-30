# backend/app/api/routes.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models.task import Task, TaskCreate
from ..services.ai_service import AIService

router = APIRouter()
ai_service = AIService()

tasks = []

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    task_dict = task.dict()
    analysis = ai_service.analyze_text(task.title + " " + (task.description or ""))
    task_dict.update({
        "id": len(tasks),
        "ai_category": analysis["category"],
        "sentiment": analysis["sentiment"]
    })
    tasks.append(task_dict)
    return task_dict

@router.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks