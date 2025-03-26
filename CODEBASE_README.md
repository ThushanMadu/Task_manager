# Task Management Application - Codebase Overview

## Project Structure

### Main Components
- `task_manager.py`: The core application file containing all functionality
- `tasks.txt`: Persistent storage file for tasks (automatically created)

## Code Architecture

### Data Structure
The application uses a list of dictionaries to store tasks. Each task is a dictionary with the following keys:
- `id`: Unique identifier for the task
- `name`: Task name
- `description`: Detailed description of the task
- `priority`: Task priority (1-5)
- `due_date`: Task deadline
- `status`: Current task status

### Key Functions Breakdown

#### Task Management Functions
1. `add_task()`
   - Prompts user for task details
   - Validates input (priority, date)
   - Creates a task dictionary
   - Adds task to the `tasks` list
   - Generates a unique ID

2. `view_tasks()`
   - Displays all tasks in a formatted table
   - Shows task details: ID, name, description, priority, due date, status
   - Handles empty task list scenario

3. `update_task()`
   - Allows updating specific task attributes
   - Provides menu for selecting which attribute to modify
   - Validates new input
   - Updates the selected task

4. `delete_task()`
   - Removes a task by its ID
   - Displays current tasks before deletion
   - Handles task not found scenarios

#### File Handling Functions
1. `load_tasks_from_file()`
   - Reads tasks from `tasks.txt`
   - Parses each line into a task dictionary
   - Handles file not found scenario
   - Clears existing tasks before loading

2. `save_tasks_to_file()`
   - Writes all tasks to `tasks.txt`
   - Uses pipe (`|`) as a delimiter for easy parsing
   - Saves task details in a consistent format

### Main Program Flow
1. Application starts
2. Automatically loads existing tasks from file
3. Displays main menu
4. Allows user to interact with tasks
5. Provides options to save/load tasks

## Input Validation
- Priority: Must be between 1-5
- Due Date: Must be in YYYY-MM-DD format
- Task ID: Validated before update/delete operations

## Error Handling
- Comprehensive try-except blocks
- User-friendly error messages
- Prevents application crashes

## Persistent Storage
- Tasks are saved between application runs
- File-based storage with simple, readable format
- Easy to backup or transfer tasks

## Best Practices Implemented
- Modular function design
- Clear separation of concerns
- Input validation
- Error handling
- User-friendly interface

## Potential Improvements
- Add task sorting
- Implement task search functionality
- Create more advanced filtering
- Add data export to other formats

## Troubleshooting
- Ensure Python 3.7+ is installed
- Check file permissions for `tasks.txt`
- Verify input formats when adding/updating tasks

## Running the Application
```bash
python task_manager.py
```

## Contributing
Feel free to fork and improve the application. 
Suggestions and pull requests are welcome!
