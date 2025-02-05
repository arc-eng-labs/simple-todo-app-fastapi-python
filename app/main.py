from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import uvicorn

from .db import get_db
from .crud import create_todo, read_todos, delete_todo

app = FastAPI()

# Mount the static directory to serve CSS and other static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure the templates directory
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_root(request: Request, db: Session = Depends(get_db)):
    todos = read_todos(db)
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add")
def add_todo_item(title: str = Form(...), db: Session = Depends(get_db)):
    create_todo(db, title)
    return {"message": "Todo added"}

@app.get("/delete/{todo_id}")
def remove_todo_item(todo_id: int, db: Session = Depends(get_db)):
    delete_todo(db, todo_id)
    return {"message": "Todo deleted"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
