from pydantic import BaseModel

class Tasks(BaseModel):
    title: str
    description: str
    completed: bool

class TasksReturn(Tasks):
    id: int