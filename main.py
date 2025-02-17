import argparse
from schemas.manager import Manager

def main():
    manager = Manager()
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    
    parser.add_argument("command", choices=[
        "add_user", "list_users", "remove_user", "add_task", "list_tasks", 
        "list_tasks_by_user", "remove_task", "export_tasks_json"
    ], help="Command to execute")
    
    parser.add_argument("--name", type=str, help="User name")
    parser.add_argument("--email", type=str, help="User email")
    parser.add_argument("--user_id", type=str, help="User ID")
    parser.add_argument("--title", type=str, help="Task title")
    parser.add_argument("--description", type=str, help="Task description")
    parser.add_argument("--status", type=str, choices=["Pending", "In Progress", "Completed"], help="Task status")
    parser.add_argument("--task_id", type=str, help="Task ID")
    parser.add_argument("--filename", type=str, default="tasks.json", help="Filename for export")
    
    args = parser.parse_args()
    
    if args.command == "add_user" and args.name and args.email:
        print(manager.add_user(args.name, args.email))
    elif args.command == "list_users":
        print("\n".join(manager.list_users()))
    elif args.command == "remove_user" and args.user_id:
        print(manager.remove_user(args.user_id))
    elif args.command == "add_task" and args.title and args.description and args.status and args.user_id:
        print(manager.add_task(args.title, args.description, args.status, args.user_id))
    elif args.command == "list_tasks":
        print("\n".join(manager.list_tasks()))
    elif args.command == "list_tasks_by_user" and args.user_id:
        print("\n".join(manager.list_tasks_by_user(args.user_id)))
    elif args.command == "remove_task" and args.task_id:
        print(manager.remove_task(args.task_id))
    elif args.command == "export_tasks_json":
        print(manager.export_tasks_json(args.filename))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
