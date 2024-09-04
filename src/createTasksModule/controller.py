from createTasksModule.types import Tasks, TasksReturn
from schemas import Task, setup_database

import os

DATABASE_URL = os.getenv('DATABASE_URL')
engine, SessionLocal = setup_database(DATABASE_URL)

db = SessionLocal()

def create_tasks_controller(task: Tasks) -> TasksReturn:
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    return new_task