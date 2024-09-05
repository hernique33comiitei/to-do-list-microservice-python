from datetime import timedelta
from fastapi import FastAPI, status
from getTasksModule.controller import get_task_by_id_controller
from globalTypes import TasksReturn

app = FastAPI()

@app.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def get_task_by_id(task_id: int) -> TasksReturn:
    return await get_task_by_id_controller(task_id=task_id)