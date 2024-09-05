from datetime import timedelta
from globalTypes import TasksReturn
from schemas import Task, defaultDatabase
import json
from config.redisConfig import redis_connection

async def get_task_by_id_controller(task_id: int) -> TasksReturn:
    db = defaultDatabase()

    redis = await redis_connection()

    cache_key = f"task:{task_id}"
    cached_task = await redis.get(cache_key)

    if cached_task:
        cached_task_dict = json.loads(cached_task)
        return TasksReturn(**cached_task_dict)
    
    task = db.query(Task).filter(Task.id == task_id).one()

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
