import uuid

class User:
    def __init__(self, name: str, email: str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.nome}, Email: {self.email}"
