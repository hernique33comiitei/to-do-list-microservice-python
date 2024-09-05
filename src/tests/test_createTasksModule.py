from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import Base, Task as TaskModel
from globalTypes import Tasks, TaskWithId
from createTasksModule.controller import create_tasks_controller  

DATABASE_URL = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestCreateTasksModule:
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

    def test_create_tasks_controller(self):
        new_task = create_tasks_controller(self.valid_task_data)

        task = self.session.query(TaskModel).filter_by(title="Title task").first()
        assert task is not None
        assert task.title == "Title task"
        assert task.description == "Description task"
        assert task.completed == False

        assert isinstance(new_task, TaskWithId)
        assert new_task.title == "Title task"
        assert new_task.description == "Description task"
