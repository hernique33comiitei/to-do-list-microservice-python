from datetime import timedelta
from fastapi import HTTPException
from sqlalchemy.orm.exc import NoResultFound
from globalTypes import TasksReturn
from schemas import Task, defaultDatabase
from config.redisConfig import redis_connection
import json

async def get_task_by_id_controller(task_id: int) -> TasksReturn:
    db = defaultDatabase()
    redis = await redis_connection()

    cache_key = f"task:{task_id}"
    cached_task = await redis.get(cache_key)

    if cached_task:
        cached_task_dict = json.loads(cached_task)
        return TasksReturn(**cached_task_dict)
    
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


    task_dict = {
        'title': task.title,
        'description': task.description,
        'completed': task.completed,
        'id': task.id
    }
    
    task_json = json.dumps(task_dict)

    expire_time = int(timedelta(seconds=30).total_seconds())
    
    await redis.setex(cache_key, expire_time, task_json)
    
    return TasksReturn(**task_dict)
