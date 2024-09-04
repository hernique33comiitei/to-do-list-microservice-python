from fastapi import FastAPI, status
from createTasksModule.types import Tasks, TasksReturn
from createTasksModule.controller import create_tasks_controller

app = FastAPI()

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
def send_tasks(task: Tasks) -> TasksReturn:
    return create_tasks_controller(task=task)