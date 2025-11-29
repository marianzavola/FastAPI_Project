from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str = "to-do"


tasks = [
    Task(
        id=1,
        title="Create API",
        description="Project 'To Do List'",
        status="in-progress"),
    Task(
        id=2,
        title="Workearly Seminar",
        description="Python basics",
        status="in-progress"
    ),
    Task(id=3,
         title="mySQL",
         description="mySQL basics",
         status="done"
    )
]

next_id = 4

@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    global next_id
    task.id = next_id
    tasks.append(task)
    next_id += 1
    return task


@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail=f"Task with id {task_id} not found")