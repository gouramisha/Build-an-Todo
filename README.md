# FastAPI Todo App

A simple Todo API built with Python and FastAPI.

## Features

- Create todos
- Read all todos
- Get a single todo by ID
- Update a todo
- Delete a todo

## Project Structure

- `main.py` - FastAPI application and routes
- `venv/` - Python virtual environment

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

## Setup

1. Activate the virtual environment:

   ```bash
   .\venv\Scripts\Activate
   ```

2. Install dependencies if needed:

   ```bash
   pip install fastapi uvicorn pydantic
   ```

3. Run the app:

   ```bash
   uvicorn main:app --reload
   ```

4. Open the API docs in your browser:

   - http://127.0.0.1:8000/docs

## API Endpoints

- `POST /todos` - create a todo
- `GET /todos` - list all todos
- `GET /todo/{todo_id}` - get one todo by ID
- `PUT /todo/{todo_id}` - update a todo
- `DELETE /todo/{todo_id}` - delete a todo

## TODO

- [ ] Fix the update route logic
- [ ] Fix the delete route logic
- [ ] Add better validation for todo data
- [ ] Add database persistence
- [ ] Add tests for API behavior
- [ ] Improve error handling and response messages
- [ ] Add authentication if needed
- [ ] Add frontend or UI for managing todos

## Notes

This project is a beginner-friendly FastAPI example and is a good starting point for learning CRUD APIs.
