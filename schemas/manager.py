import json
import uuid
from schemas.user import User
from schemas.task import Task

USER_FILE = "database/users.json"
TASK_FILE = "database/tasks.json"

class Manager:
    def __init__(self):
        self.users = self.load_users()
        self.tasks = self.load_tasks()
    
    def load_users(self):
        try:
            with open(USER_FILE, "r", encoding="utf-8") as f:
                users_data = json.load(f)
                return [User(user["user_id"],
                             user["name"],
                             user["email"]
                            ) for user in users_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_users(self):
        with open(USER_FILE, "w", encoding="utf-8") as f:
            json.dump([{"user_id": u.user_id,
                        "name": u.name,
                        "email": u.email
                       } for u in self.users], f, indent=4, ensure_ascii=False)
    
    def load_tasks(self):
        try:
            with open(TASK_FILE, "r", encoding="utf-8") as f:
                tasks_data = json.load(f)
                return [Task(task["task_id"], 
                             task["title"], 
                             task["description"], 
                             task["status"], 
                             self.get_user_by_id(task["user_id"])) 
                             for task in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def save_tasks(self):
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            json.dump([{
                "task_id": t.task_id,
                "title": t.title,
                "description": t.description,
                "status": t.status,
                "user_id": t.user.user_id
                } for t in self.tasks], f, indent=4, ensure_ascii=False)
    
    def get_user_by_id(self, user_id: str):
        return next((u for u in self.users if u.user_id == user_id), None)
    
    def add_user(self, name: str, email: str):
        user_id = str(uuid.uuid4())
        user = User(user_id, name, email)
        self.users.append(user)
        self.save_users()
        return f"User {user.name} added successfully! ID: {user.user_id}"
    
    def list_users(self):
        return [str(user) for user in self.users]
    
    def remove_user(self, user_id: str):
        user = self.get_user_by_id(user_id)
        if not user:
            return "User not found!"
        
        self.tasks = [t for t in self.tasks if t.user.user_id != user_id]
        self.users.remove(user)
        self.save_users()
        self.save_tasks()
        return f"User {user.name} removed successfully!"
    
    def get_task_by_id(self, task_id: str):
        return next((t for t in self.tasks if t.task_id == task_id), None)
    
    def add_task(self, title: str, description: str, status: str, user_id: str):
        user = self.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found!")
        
        task_id = str(uuid.uuid4())
        task = Task(task_id, title, description, status, user)
        self.tasks.append(task)
        self.save_tasks()
        return f"Task '{title}' assigned to {user.name}."
    
    def list_tasks(self):
        return [str(task) for task in self.tasks]
    
    def list_tasks_by_user(self, user_id: str):
        user_tasks = [task for task in self.tasks if task.user.user_id == user_id]
        return [str(task) for task in user_tasks] if user_tasks else "No tasks found for this user."
    
    def remove_task(self, task_id: str):
        task = next((t for t in self.tasks if t.task_id == task_id), None)
        if not task:
            return "Task not found!"
        
        self.tasks.remove(task)
        self.save_tasks()
        return f"Task '{task.title}' removed successfully!"
    
    def update_task_status(self, task_id: str, new_status: int):
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status not in range(3):
            return "Invalid status! Choose from: 0 - Pending, 1 - In Progress, 2 - Completed."
        
        task = self.get_task_by_id(task_id)
        if not task:
            return "Task not found!"
        
        task.status = valid_statuses[new_status]
        self.save_tasks()
        return f"Task '{task.title}' status updated to {new_status}!"
