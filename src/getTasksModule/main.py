from typing import List
from fastapi import FastAPI, status
from getTasksModule.controller import get_all_task_controller, get_task_by_id_controller
from globalTypes import ErrorResponse, TaskWithId

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
async def get_task_by_id(task_id: int) -> TaskWithId:
    return await get_task_by_id_controller(task_id=task_id)

@app.get(
    "/tasks/",
    response_model=List[TaskWithId],
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Task not found"
        }
    },
    status_code=status.HTTP_200_OK
)
async def get_all_tasks() -> List[TaskWithId]:
    return await get_all_task_controller()