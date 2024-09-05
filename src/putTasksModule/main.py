from fastapi import FastAPI, status
from globalTypes import ErrorResponse, TaskWithId, Tasks
from putTasksModule.controller import put_task_by_id_controller
from schemas import defaultDatabase

app = FastAPI()

@app.put(
    "/tasks/{task_id}",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Task not found"
        }
    },
    status_code=status.HTTP_200_OK
)
async def put_task_by_id(task_id: int, task_update: Tasks) -> TaskWithId:
    db = defaultDatabase()
    return await put_task_by_id_controller(task_id=task_id, task_update=task_update, db=db)