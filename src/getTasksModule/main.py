from datetime import timedelta
from fastapi import FastAPI, status
from getTasksModule.controller import get_task_by_id_controller
from globalTypes import ErrorResponse, TasksReturn
from schemas import Task

app = FastAPI()

@app.get(
    "/tasks/{task_id}",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Task not found"
        }
    },
    status_code=status.HTTP_200_OK
)
async def get_task_by_id(task_id: int) -> TasksReturn:
    return await get_task_by_id_controller(task_id=task_id)