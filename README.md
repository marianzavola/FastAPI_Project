  Simple Task API (FastAPI)

This project is a foundational Task API built using FastAPI and Pydantic. 
It allows users to perform basic Read and Create operations on a collection of tasks.


  Features

1) View All Tasks: Retrieve a list of all existing tasks.

2) Create Task: Add a new task with a title and description.

3) View Task by ID: Fetch details for a specific task.

4) In-Memory Storage: Uses a simple Python list for data storage (data is reset when the server restarts).


  Technology

Backend Framework: FastAPI

Data Validation: Pydantic

Language: Python 3.14


  Installation

1) Clone the repository:
   
git clone [YOUR_REPO_URL]
cd [YOUR_REPO_NAME]

3) Install the required dependencies:
   
install fastapi uvicorn pydantic

5) Run the application using Uvicorn:
   
uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000 .

Next Steps

1) Implement PUT and DELETE operations for complete task management.
2) Connect the API to a persistent database so data isn't lost on server restart.
3) Kanban Structure: Implement separate endpoints for Boards and Lists to organize tasks better.
