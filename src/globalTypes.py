from typing import Optional
from pydantic import BaseModel

class Tasks(BaseModel):
    title: str
    description: str
    completed: bool

class TaskWithId(Tasks):
    id: int

    class Config:
        from_attributes = True

class PartialTasks(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class ErrorResponse(BaseModel):
    errorMessage: str
    errorCode: int
    errorDescription: str
