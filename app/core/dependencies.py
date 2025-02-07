

from app.core.database import SessionLocal

from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
