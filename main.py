from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Optional
from uuid import UUID, uuid4 # Unique identifier

app = FastAPI()

class Task(BaseModel): # FastAPI will convert the pydantic model to JSON automatically
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


tasks = []


@app.post("/task/", response_model=Task) # POST request
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task) # Appending to the memory db
    return task

@app.get("/task",response_model=List[Task]) # GET request
def read_task():
    return tasks

@app.get("/task/{task.id}", response_model=Task) # GET a specific task
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task

    return HTTPException(status_code=404, detail="Task not found")

@app.put("/task/{task.id}",response_model=Task) # PUT request(updating)
def update_task(task_id: UUID, task_update: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            task[index] = updated_task
            return updated_task
        
    raise HTTPException(status_code=404,detail="Task not found")

@app.delete("/task/{task_id}",response_model=Task) # DELETE request
def delete_task(task_id: UUID):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop[index]
        
    raise HTTPException(status_code=404,detail="Task not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)