from fastapi import FastAPI, status
from deleteTasksModule.controller import delete_task_by_id_controller
from globalTypes import ErrorResponse, TaskWithId
from schemas import defaultDatabase

app = FastAPI()

@app.delete(
    "/tasks/{task_id}",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "Task not found"
        }
    },
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task_by_id(task_id: int) -> None:
    db = defaultDatabase()
    return await delete_task_by_id_controller(task_id=task_id,db=db)