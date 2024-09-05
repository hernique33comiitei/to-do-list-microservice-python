from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createTasksModule.controller import create_tasks_controller
from getTasksModule.controller import get_all_task_controller, get_task_by_id_controller
from globalTypes import TaskWithId, Tasks
from schemas import Base
import pytest

DATABASE_URL = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestGetTaskById:
    @classmethod
    def setup_class(cls):
        Base.metadata.create_all(engine)
        cls.session = SessionLocal()
        cls.valid_task = Tasks(
            title="Title task",
            description="Description task",
            completed=False
        )

    @classmethod
    def teardown_class(cls):
        cls.session.rollback()
        cls.session.close()

    @pytest.mark.asyncio
    async def test_get_task_by_id_controller(self):
        db = SessionLocal()

        new_task = create_tasks_controller(task=self.valid_task, db=db)
        new_task_dict: TaskWithId = TaskWithId.model_validate(new_task).model_dump()

        task = await get_task_by_id_controller(task_id=new_task_dict["id"] , db=db)
        task_dict: TaskWithId = TaskWithId.model_validate(task).model_dump()
        
        assert task_dict["title"] == "Title task"
        assert task_dict["title"] != "title"
        assert task_dict["description"] == "Description task"
        assert task_dict["description"] != "description"
        assert task_dict["completed"] == False

