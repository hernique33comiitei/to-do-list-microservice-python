from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createTasksModule.controller import create_tasks_controller
from putTasksModule.controller import put_task_by_id_controller
from schemas import Base
from globalTypes import Tasks, TaskWithId
import pytest

DATABASE_URL = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestPutTasksModule:
    @classmethod
    def setup_class(cls):
        Base.metadata.create_all(engine)
        cls.session = SessionLocal()
        cls.valid_task_data = Tasks(
            title="Title task",
            description="Description task",
            completed=False 
        )
        cls.updated_task_data = Tasks(
            title="Title update",
            description="Description update",
            completed=True 
        )

    @classmethod
    def teardown_class(cls):
        cls.session.rollback()
        cls.session.close()

    @pytest.mark.asyncio
    async def test_put_task_by_id_controller(self):
        db = SessionLocal()

        new_task = create_tasks_controller(self.valid_task_data, db=db)
        task_to_put_dict: TaskWithId = TaskWithId.model_validate(new_task).model_dump()

        task_id = task_to_put_dict["id"]
        task_updated = await put_task_by_id_controller(task_id=task_id, task_update=self.updated_task_data, db=db)
        task_updated_dict: TaskWithId = TaskWithId.model_validate(task_updated).model_dump()

        assert task_updated_dict["title"] == "Title update"
        assert task_updated_dict["description"] == "Description update"
        assert task_updated_dict["completed"] == True


