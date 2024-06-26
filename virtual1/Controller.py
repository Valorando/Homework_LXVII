from fastapi import FastAPI, HTTPException
from Service import Get_all_tasks, Add_task, Edit_task, Delete_task

app = FastAPI(
    title="ToDo List"
)

@app.get("/tasks/")
def get_tasks():
    tasks = Get_all_tasks()
    return tasks

@app.post("/tasks/")
def create_task(task: str, status: str):
    try:
        Add_task(task, status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return("Задача успешно добавлена")

@app.put("/tasks/")
def update_task(task_name: str, new_task: str, new_status:str):
    try:
        Edit_task(task_name, new_task, new_status)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return("Задача успешно обновлена")

@app.delete("/tasks/")
def remove_task(task_name: str):
    try:
        Delete_task(task_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return("Задача успешно удалена")