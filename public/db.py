from sqlalchemy import create_engine, text
from sqlalchemy import insert, select
from models.good import Base, User
from config import settings

ur_s = settings.POSTGRES_DATABASE_URLS
engine_s = create_engine(ur_s, echo=True)


def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)


def f():
    with engine_s.connect() as conn:
        answer = conn.execute(text('select * from users;'))
        print(f"answer = {answer.all()}")


def f_bilder():
    with engine_s.connect() as conn:
        query = insert(User).values([
            {"name": "Sidorov", "hashed_password": "12345"}
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(User)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")
