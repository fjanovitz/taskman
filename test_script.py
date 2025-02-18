import subprocess

def run_command(command):
    print(f"Running command: {command}")  # Debugging line
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(f"Command output: {result.stdout.strip()}")  # Debugging line
    return result.stdout.strip()

def extract_user_id(output):
    print(f"Extracting user ID from output: {output}")  # Debugging line
    parts = output.split("ID: ")
    return parts[1] if len(parts) > 1 else None

def main():
    print("Adicionando usuários...")
    alice_output = run_command("python main.py add_user --name Alice --email alice@email.com")
    bob_output = run_command("python main.py add_user --name Bob --email bob@email.com")
    
    alice_id = extract_user_id(alice_output)
    bob_id = extract_user_id(bob_output)
    
    print(f"Alice ID: {alice_id}")  # Debugging line
    print(f"Bob ID: {bob_id}")  # Debugging line
    
    print("\nAdicionando tarefas...")
    if alice_id:
        run_command(f"python main.py add_task --title 'Revisar Documentação' --description 'Revisar a documentação do projeto' --status 'Pending' --user_id {alice_id}")
        run_command(f"python main.py add_task --title 'Testar Funcionalidades' --description 'Realizar testes unitários' --status 'Pending' --user_id {alice_id}")
    
    if bob_id:
        run_command(f"python main.py add_task --title 'Desenvolver API' --description 'Criar endpoints REST para o sistema' --status 'In Progress' --user_id {bob_id}")
    
    print("\nTarefas cadastradas:")
    run_command("python main.py list_tasks")

if __name__ == "__main__":
    main()