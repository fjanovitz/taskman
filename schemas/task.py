import uuid
from user import User

class Task:
    STATUS_OPTIONS = ["Pending", "In Progress", "Completed"]
    
    def __init__(self, title: str, description: str, status: str, user: User):
        if status not in self.STATUS_OPTIONS:
            raise ValueError("Invalid status. Choose from: Pending, In Progress, Completed.")
        
        self.task_id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.user = user
    
    def __str__(self):
        return f"ID: {self.task_id}, Title: {self.title}, Status: {self.status}, Assigned to: {self.user.name}"
