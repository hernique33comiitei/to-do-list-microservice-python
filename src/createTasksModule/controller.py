from globalTypes import Tasks, TaskWithId
from schemas import Task
from sqlalchemy.orm import Session

def create_tasks_controller(task: Tasks, db: Session) -> TaskWithId:    
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task