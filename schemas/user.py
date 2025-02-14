import json

class User:
    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.nome}, Email: {self.email}"
