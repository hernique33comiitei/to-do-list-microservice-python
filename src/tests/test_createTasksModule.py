from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import Base, Task

DATABASE_URL = 'sqlite:///:memory:'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TestTask:
    @classmethod
    def setup_class(cls):
        Base.metadata.create_all(engine)
        cls.session = SessionLocal()
        cls.valid_task = Task(
            title="Title task",
            description="Description task"
        )

    @classmethod
    def teardown_class(cls):
        cls.session.rollback()
        cls.session.close()

    def test_create_tasks_controller(self):
        self.session.add(self.valid_task)
        self.session.commit()

        task = self.session.query(Task).filter_by(title="Title task").first()
        assert task.title == "Title task"
        assert task.title != "title"
        assert task.description == "Description task"
        assert task.description != "description"
        assert task.completed == False
