from sqlalchemy.orm import Session

from . import models, schemas


def create_todo(db: Session, title: str):
    db_todo = models.Todo(title=title)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def read_todos(db: Session):
    return db.query(models.Todo).all()


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
