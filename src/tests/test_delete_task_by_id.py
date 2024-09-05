from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createTasksModule.controller import create_tasks_controller
from getTasksModule.controller import get_task_by_id_controller
from schemas import Base
from globalTypes import Tasks, TaskWithId
from deleteTasksModule.controller import delete_task_by_id_controller
import pytest

DATABASE_URL = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestDeleteTaskById:
    @classmethod
    def setup_class(cls):
        Base.metadata.create_all(engine)
        cls.session = SessionLocal()
        cls.valid_task_data = Tasks(
            title="Title task",
            description="Description task",
            completed=False 
        )

    @classmethod
    def teardown_class(cls):
        cls.session.rollback()
        cls.session.close()

    @pytest.mark.asyncio
    async def test_delete_task_by_id_controller(self):
        db = SessionLocal()

        new_task = create_tasks_controller(self.valid_task_data, db=db)
        task_to_delete_dict: TaskWithId = TaskWithId.model_validate(new_task).model_dump()

        task_id = task_to_delete_dict["id"]
        await delete_task_by_id_controller(task_id=task_id, db=db)

        with pytest.raises(HTTPException) as excinfo:
                await get_task_by_id_controller(task_id, db=db)

        assert excinfo.value.status_code == 404


