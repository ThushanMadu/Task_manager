import os
from datetime import datetime

# List to store tasks
tasks = []

def add_task():
    """
    Add a new task to the tasks list.
    Prompts user for task details and creates a task dictionary.
    """
    print("\n--- Add New Task ---")
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    
    # Priority validation
    while True:
        try:
            priority = int(input("Enter task priority (1-5, where 1 is highest): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer for priority.")
    
    # Due date validation
    while True:
        try:
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    # Create task dictionary
    task = {
        'id': len(tasks) + 1,
        'name': name,
        'description': description,
        'priority': priority,
        'due_date': due_date_str,
        'status': 'Pending'
    }
    
    tasks.append(task)
    print("Task added successfully!")
    return task

def view_tasks():
    """
    Display all tasks in a formatted manner.
    """
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n--- Current Tasks ---")
    print("-" * 80)
    print(f"{'ID':<5}{'Name':<20}{'Description':<25}{'Priority':<10}{'Due Date':<15}{'Status':<10}")
    print("-" * 80)
    
    for task in tasks:
        print(f"{task['id']:<5}{task['name']:<20}{task['description']:<25}{task['priority']:<10}{task['due_date']:<15}{task['status']:<10}")
    print("-" * 80)

def update_task():
    """
    Update an existing task by its ID.
    """
    view_tasks()
    if not tasks:
        return
    
    try:
        task_id = int(input("Enter the ID of the task you want to update: "))
        task = next((t for t in tasks if t['id'] == task_id), None)
        
        if not task:
            print("Task not found.")
            return
        
        print("\nSelect what you want to update:")
        print("1. Name")
        print("2. Description")
        print("3. Priority")
        print("4. Due Date")
        print("5. Status")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task['name'] = input("Enter new task name: ")
        elif choice == '2':
            task['description'] = input("Enter new description: ")
        elif choice == '3':
            while True:
                try:
                    priority = int(input("Enter new priority (1-5): "))
                    if 1 <= priority <= 5:
                        task['priority'] = priority
                        break
                    else:
                        print("Priority must be between 1 and 5.")
                except ValueError:
                    print("Please enter a valid integer.")
        elif choice == '4':
            while True:
                try:
                    due_date_str = input("Enter new due date (YYYY-MM-DD): ")
                    datetime.strptime(due_date_str, "%Y-%m-%d")
                    task['due_date'] = due_date_str
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == '5':
            status_options = ['Pending', 'In Progress', 'Completed']
            print("Status Options:")
            for i, status in enumerate(status_options, 1):
                print(f"{i}. {status}")
            
            while True:
                try:
                    status_choice = int(input("Select status (1-3): "))
                    if 1 <= status_choice <= 3:
                        task['status'] = status_options[status_choice - 1]
                        break
                    else:
                        print("Invalid choice. Please select 1-3.")
                except ValueError:
                    print("Please enter a valid number.")
        
        print("Task updated successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def delete_task():
    """
    Delete a task by its ID.
    """
    view_tasks()
    if not tasks:
        return
    
    try:
        task_id = int(input("Enter the ID of the task you want to delete: "))
        task = next((t for t in tasks if t['id'] == task_id), None)
        
        if task:
            tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found.")
    
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def load_tasks_from_file(filename='tasks.txt'):
    """
    Load tasks from a text file.
    """
    global tasks
    tasks.clear()
    
    if not os.path.exists(filename):
        return
    
    with open(filename, 'r') as file:
        for line in file:
            # Split the line and create task dictionary
            task_data = line.strip().split('|')
            if len(task_data) == 6:
                task = {
                    'id': int(task_data[0]),
                    'name': task_data[1],
                    'description': task_data[2],
                    'priority': int(task_data[3]),
                    'due_date': task_data[4],
                    'status': task_data[5]
                }
                tasks.append(task)
    
    print(f"Loaded {len(tasks)} tasks from file.")

def save_tasks_to_file(filename='tasks.txt'):
    """
    Save tasks to a text file.
    """
    with open(filename, 'w') as file:
        for task in tasks:
            # Use '|' as a delimiter for easy parsing
            task_line = f"{task['id']}|{task['name']}|{task['description']}|{task['priority']}|{task['due_date']}|{task['status']}\n"
            file.write(task_line)
    
    print(f"Saved {len(tasks)} tasks to file.")

def main_menu():
    """
    Display main menu and handle user interactions.
    """
    while True:
        print("\n--- Task Management Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save Tasks to File")
        print("6. Load Tasks from File")
        print("7. Exit")
        
        try:
            choice = input("Enter your choice (1-7): ")
            
            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                update_task()
            elif choice == '4':
                delete_task()
            elif choice == '5':
                save_tasks_to_file()
            elif choice == '6':
                load_tasks_from_file()
            elif choice == '7':
                print("Exiting Task Management Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Load existing tasks when the application starts
    load_tasks_from_file()
    
    # Start the main menu
    main_menu()
