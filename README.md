# Notes API with Version History & Authentication

A secure and robust backend API built with Python and FastAPI that allows users to create, manage, and track version history for their notes. This project demonstrates a deep understanding of modern backend principles, including REST API design, database modeling with SQLAlchemy, JWT-based authentication, and clean, layered architecture.

## Features

-   **User Authentication**: Secure user registration and login using JWT (JSON Web Tokens). Passwords are never stored in plain text, only securely hashed using `bcrypt`.
-   **Full CRUD Operations for Notes**: Users can Create, Read, Update, and Delete their notes.
-   **Per-User Isolation**: Users can only access and manage their own notes, ensuring data privacy and security.
-   **Note Version History**: Every time a note is updated, its previous state is saved, creating a complete version history for each note.
-   **Interactive API Documentation**: Automatically generated, interactive API documentation (via Swagger UI) for easy testing and exploration.

## Technology Stack

-   **Backend**: Python 3.8+
-   **API Framework**: FastAPI
-   **Database**: SQLite
-   **ORM**: SQLAlchemy
-   **Data Validation**: Pydantic
-   **Authentication**: JWT & `bcrypt`
-   **Web Server**: Uvicorn

## API Endpoints

All endpoints are prefixed with `/api/v1`.

| Method | Endpoint             | Description                      | Authentication |
| :----- | :------------------- | :------------------------------- | :------------- |
| `POST` | `/auth/register`     | Register a new user.             | None           |
| `POST` | `/auth/token`        | Log in to get an access token.   | None           |
| `POST` | `/notes/`            | Create a new note.               | Required       |
| `GET`  | `/notes/`            | Get all notes for the user.      | Required       |
| `GET`  | `/notes/{note_id}`   | Get a specific note.             | Required       |
| `PUT`  | `/notes/{note_id}`   | Update a specific note.          | Required       |
| `DELETE`| `/notes/{note_id}`  | Delete a specific note.          | Required       |
| `GET`  | `/notes/{note_id}/history` | Get the version history of a note. | Required |


## Getting Started

Follow these instructions to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/notes-api-project.git
cd notes-api-project
```
*(Replace `your-username` with your actual GitHub username)*

### 2. Create and Activate a Virtual Environment

*   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
*   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### 3. Install Dependencies
With your virtual environment activated, install the necessary packages using pip:
```bash
pip install "fastapi[all]" sqlalchemy passlib[bcrypt] python-jose
```

### 4. Run the API Server
Start the development server from the main project directory:
```bash
uvicorn main:app --reload
```
The API will be available at `http://12.0.0.1:8000`.

## Usage

Once the server is running, navigate to **`http://127.0.0.1:8000/docs`** in your web browser to access the interactive API documentation.

From there you can:
1.  Register a user with `/auth/register`.
2.  Log in with `/auth/token`.
3.  Click the "Authorize" button and enter your token as `Bearer <YOUR_TOKEN>`.
4.  Test all the secure note endpoints!
