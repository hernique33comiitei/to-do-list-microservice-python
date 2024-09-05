from fastapi import HTTPException
from sqlalchemy.orm.exc import NoResultFound
from globalTypes import TaskWithId, Tasks
from schemas import Task
from sqlalchemy.orm import Session

async def put_task_by_id_controller(task_id: int, task_update: Tasks, db: Session) -> TaskWithId:
    try:
        task = db.query(Task).filter(Task.id == task_id).one()
    except NoResultFound:
        raise HTTPException(
            status_code=404,
            detail={
                "errorMessage": "There is no task with this id",
                "errorCode": 404,
                "errorDescription": "It was not possible to find any task with this id in the database"
            }
        )
        
    for key, value in task_update.model_dump().items():
        setattr(task, key, value)
    
    db.commit()
    
    return TaskWithId.model_validate(task)

    