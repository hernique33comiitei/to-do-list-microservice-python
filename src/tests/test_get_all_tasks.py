from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createTasksModule.controller import create_tasks_controller
from getTasksModule.controller import get_all_task_controller
from globalTypes import TaskWithId
from schemas import Base
import pytest

DATABASE_URL = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestGetAllTasks:
    @classmethod
    def setup_class(cls):
        Base.metadata.create_all(engine)
        cls.session = SessionLocal()
        cls.list_valid_tasks = [
            TaskWithId(title="title1",description="description1",completed=False,id=1),
            TaskWithId(title="title2",description="description2",completed=True,id=2),
            TaskWithId(title="title3",description="description3",completed=False,id=3)
        ]

    @classmethod
    def teardown_class(cls):
        cls.session.rollback()
        cls.session.close()

    @pytest.mark.asyncio
    async def test_get_all_task(self):
        db = SessionLocal()

        for i in self.list_valid_tasks:
            create_tasks_controller(task=i, db=db)
        
        get_tasks = await get_all_task_controller(db=db)

        for index, v in enumerate(get_tasks):
            get_task_dict: TaskWithId = TaskWithId.model_validate(v).model_dump()
            
            list_valid_tasks_index: TaskWithId = TaskWithId.model_validate(self.list_valid_tasks[index]).model_dump()
            
            assert get_task_dict["title"] == list_valid_tasks_index["title"]

            


