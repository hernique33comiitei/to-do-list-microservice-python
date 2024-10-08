from datetime import timedelta
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm.exc import NoResultFound
from globalTypes import TaskWithId
from schemas import Task, defaultDatabase
from config.redisConfig import redis_connection
import json
from sqlalchemy.orm import Session

async def get_task_by_id_controller(task_id: int, db: Session) -> TaskWithId:
    redis = await redis_connection()

    cache_key = f"task:{task_id}"
    cached_task = await redis.get(cache_key)

    if cached_task:
        cached_task_dict = json.loads(cached_task)
        return cached_task_dict
    
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

    task_dict: TaskWithId = TaskWithId.model_validate(task).model_dump()
    task_json = json.dumps(task_dict)

    expire_time = int(timedelta(seconds=30).total_seconds())
    await redis.setex(cache_key, expire_time, task_json)
    
    return task_dict



async def get_all_task_controller(db: Session) -> List[TaskWithId]:
    redis = await redis_connection()

    cache_key = "task:get_all"
    cached_task = await redis.get(cache_key)

    if cached_task:
        cached_task_dict: List[TaskWithId] = json.loads(cached_task)
        return cached_task_dict
    
    try:
        task_dicts: List[TaskWithId] = []
        for task in db.query(Task).all():
            task_dicts.append(TaskWithId.model_validate(task).model_dump())
        
    except NoResultFound:
        raise HTTPException(
            status_code=404,
            detail={
                "errorMessage": "No tasks found",
                "errorCode": 404,
                "errorDescription": "Could not find any task in the database"
            }
        )

    task_json = json.dumps(task_dicts)

    expire_time = int(timedelta(seconds=30).total_seconds())
    await redis.setex(cache_key, expire_time, task_json)
    
    return task_dicts