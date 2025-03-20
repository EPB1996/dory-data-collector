# Dory Backend

## Setting Up a Virtual Environment

To create and activate a virtual environment, follow these steps:

1. Create a virtual environment:
    ```sh
    uv venv
    ```

2. Activate the virtual environment:
    - On Linux or macOS:
        ```sh
        source .venv/bin/activate
        ```
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```

## Install dependencies

1. Install Uvicorn:
    ```sh
    uv sync
    ```

2. Run the FastAPI application:
    ```sh
    uv run uvicorn main:app --reload
    ```

This will start the FastAPI server, and you can access it at `http://127.0.0.1:8000`.