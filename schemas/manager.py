import json
import uuid
from user import User
from task import Task

class Manager:
    def __init__(self):
        self.users = []
        self.tasks = []
    
    def add_user(self, name: str, email: str):
        user = User(name, email)
        self.users.append(user)
        return f"User {name} added successfully!"
    
    def remove_user(self, user_id: str):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            return "User not found!"
        
        self.tasks = [t for t in self.tasks if t.user.user_id != user_id]
        self.users.remove(user)
        return f"User {user.name} removed successfully!"
    
    def list_users(self):
        return [str(user) for user in self.users]
    
    def add_task(self, title: str, description: str, status: str, user_id: str):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if not user:
            raise ValueError("User not found!")
    
        task = Task(title, description, status, user)
        self.tasks.append(task)
        return f"Task '{title}' assigned to {user.nome}."
    
    def remove_task(self, task_id: str):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task:
            return "Task not found!"
        
        self.tasks.remove(task)
        return f"Task '{task.title}' removed successfully!"
    
    def list_all_tasks(self):
        return [str(task) for task in self.tasks]
    
    def list_tasks_user(self, user_id: str):
        user_tasks = [task for task in self.tasks if task.user.user_id == user_id]
        return [str(task) for task in user_tasks] if user_tasks else "No tasks found for this user."
    
    def export_tasks_json(self, filename="tasks.json"):
        data = [
            {
                "task_id": t.task_id,
                "title": t.title,
                "description": t.description,
                "status": t.status,
                "user": {
                    "user_id": t.user.user_id,
                    "name": t.user.nome,
                    "email": t.user.email
                }
            }
            for t in self.tasks
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return f"Tasks exported to {filename}"
