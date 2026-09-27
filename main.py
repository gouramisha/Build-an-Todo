from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 

todos =[]
class Todo (BaseModel):
    id : int
    title : str
    completed : bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"Todo added" , "data" : "Todo"}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todo/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error":"Todo not Found"}

@app.put("/todo/{todo_id}")
def update_todo(todo_id:int, update:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todo[index] = updated_todo
            return {
                "message": "updated data",
                "data" : updated_todo
            }
        
        
    return {"error":"Todo not Found"}

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id:int, update:Todo):
    for pop,todo in enumerate(todos):
        if todo.id == todo_id:
            todo[pop] = delete_todo
            return {
                "message": "delete data",
                "data" : delete_todo
            }
        
        
    return {"error":"Todo not Found"}


