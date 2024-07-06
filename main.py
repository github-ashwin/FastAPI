from fastapi import FastAPI
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

@app.get('/')
def read():
    return {'hello':'word'}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)