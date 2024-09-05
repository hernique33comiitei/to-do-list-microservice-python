from globalTypes import Tasks, TasksReturn
from schemas import Task, defaultDatabase

db = defaultDatabase()

def create_tasks_controller(task: Tasks) -> TasksReturn:
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    return new_task