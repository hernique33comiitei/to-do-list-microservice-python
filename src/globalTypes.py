from pydantic import BaseModel

class Tasks(BaseModel):
    title: str
    description: str
    completed: bool

class TaskWithId(Tasks):
    id: int

    class Config:
        from_attributes = True

class ErrorResponse(BaseModel):
    errorMessage: str
    errorCode: int
    errorDescription: str
