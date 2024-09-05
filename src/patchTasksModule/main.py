from fastapi import FastAPI, status
from globalTypes import ErrorResponse, PartialTasks, TaskWithId
from patchTasksModule.controller import patch_task_by_id_controller
from schemas import defaultDatabase

app = FastAPI()

@app.patch(
    "/tasks/{task_id}",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Task not found"
        }
    },
    status_code=status.HTTP_200_OK
)
async def patch_task_by_id(task_id: int, task_update: PartialTasks) -> TaskWithId:
    db = defaultDatabase()
    return await patch_task_by_id_controller(task_id=task_id, task_update=task_update, db=db)