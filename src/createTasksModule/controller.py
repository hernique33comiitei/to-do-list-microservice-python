from globalTypes import Tasks, TaskWithId
from schemas import Task, defaultDatabase

db = defaultDatabase()

def create_tasks_controller(task: Tasks) -> TaskWithId:
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    return new_task