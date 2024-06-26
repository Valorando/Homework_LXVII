import os
import json
import mysql.connector

config_file = os.path.join(os.path.dirname(__file__), 'configuration.json')
with open(config_file, 'r') as file:
    config = json.load(file)


db = mysql.connector.connect(
    host = config['Host'],
    user = config['User'],
    password = config['Password'],
    database = config['Database']
)

cursor = db.cursor()

def Get_all_tasks():
        cursor.execute(config['Get_all_tasks_request'])
        results = cursor.fetchall()
        tasks = []
        for row in results:
            task = {
                'task': row[0],
                'status': row[1]
            }
            tasks.append(task)
        return tasks

def Add_task(task, status):
     cursor.execute(config['Add_task_request'], (task, status))
     db.commit()

def Edit_task(task_name, new_task, new_status):
     cursor.execute(config['Edit_task_request'], (new_task, new_status, task_name))
     db.commit()
     
def Delete_task(task_name):
     cursor.execute(config['Delete_task_request'], (task_name,))
     db.commit()