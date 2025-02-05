# Simple Todo App with FastAPI and Poetry

## Project Description

This project is a simple Todo application built with Python, FastAPI, and SQLite. It includes a minimal user interface for creating and viewing todo items, and uses Poetry for dependency management.

## Features

- FastAPI backend with CRUD operations
- SQLite database for data storage
- Minimal UI (HTML, CSS) to view and add todos
- Poetry for managing project dependencies
- Example test file

## Project Structure

```
.
├── README.md               # Project documentation
├── pyproject.toml          # Poetry configuration
├── app
│   ├── main.py             # Main FastAPI application entrypoint
│   ├── db.py               # Database connection and session handling
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── crud.py             # CRUD operations for the Todo model
│   ├── templates
│   │   └── index.html      # Jinja2 template for UI
│   └── static
│       └── style.css       # CSS styles for the UI
└── tests
    └── test_main.py        # Basic test for the application
```

## Installation

1. Ensure you have Python 3.7+ installed.
2. Install [Poetry](https://python-poetry.org/docs/#installation).
3. Clone this repository.
4. Navigate to the project directory.
5. Run `poetry install` to install dependencies.

## Usage

1. Activate the virtual environment: `poetry shell`.
2. Start the FastAPI server: `uvicorn app.main:app --reload`.
3. Open your browser at `http://127.0.0.1:8000`.
4. Use the UI to add, view, or remove todo items.

## Testing

Run the tests with:

```
poetry run pytest
```

## Contributing

Feel free to submit issues or pull requests if you want to improve this project.

## License

This project is licensed under the MIT License.
