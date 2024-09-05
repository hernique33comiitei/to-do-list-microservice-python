from fastapi import FastAPI, status
from globalTypes import Tasks, TaskWithId
from createTasksModule.controller import create_tasks_controller

app = FastAPI()

@app.post("/tasks/", status_code=status.HTTP_201_CREATED)
def send_tasks(task: Tasks) -> TaskWithId:
    return create_tasks_controller(task=task)