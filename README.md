# Task Management Application

## Project Overview
This Task Management Application is designed to help users manage their tasks efficiently using Python. The application supports basic CRUD (Create, Read, Update, Delete) operations and provides file persistence for tasks.

## Features
- Add new tasks with details like name, description, priority, and due date
- View all existing tasks
- Update task details
- Delete tasks
- Save tasks to a text file
- Load tasks from a text file

## Requirements
- Python 3.7+
- No external libraries required

## How to Run
1. Ensure you have Python installed
2. Navigate to the directory containing `task_manager.py`
3. Run the application using: `python task_manager.py`

## Usage Instructions
- When the application starts, it will automatically load any existing tasks from `tasks.txt`
- Use the menu options to:
  1. Add a new task
  2. View all tasks
  3. Update an existing task
  4. Delete a task
  5. Save current tasks to file
  6. Load tasks from file
  7. Exit the application

## Task Details
Each task includes:
- Unique ID
- Name
- Description
- Priority (1-5, where 1 is highest)
- Due Date
- Status (Pending, In Progress, Completed)

## File Persistence
- Tasks are saved to and loaded from `tasks.txt`
- Tasks are stored in a pipe-delimited format for easy parsing

## Submission Details
- Stage 1 Deadline: Monday, 10th Mar 2025, at 1:00 PM
- Stage 2 Deadline: Thursday, 27th Mar 2025, at 1:00 PM

## Author
Created as part of a task management application project.
