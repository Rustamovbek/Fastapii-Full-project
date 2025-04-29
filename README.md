# 🚀 FastAPI Task Management API with JWT Authentication

![Build](https://img.shields.io/github/actions/workflow/status/theMirmakhmudov/FastAPI-Task-JWT/ci.yml?label=CI&style=flat-square)
![Build](https://img.shields.io/github/actions/workflow/status/theMirmakhmudov/FastAPI-Task-JWT/ci.yml?label=CD&style=flat-square)
![License](https://img.shields.io/github/license/theMirmakhmudov/FastAPI-Task-JWT?style=flat-square)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat-square)

> A simple, secure and modern **FastAPI** project for task management with **JWT authentication**.

---

## 🔧 Features

- 🔐 JWT Authentication (Login & Registration)
- 📝 Task CRUD operations (Create, Read, Update, Delete)
- 👤 User-specific task management
- 📦 Modern Python stack (FastAPI, Pydantic, SQLAlchemy)
- 📄 Swagger UI & ReDoc documentation (auto-generated)
- 🧪 Pytest-based test structure (optional)

---

## 🖥️ API Endpoints

### 🔐 Auth

| Method | Endpoint       | Description         |
|--------|----------------|---------------------|
| POST   | `/register`    | Register a new user |
| POST   | `/login`       | Log in with credentials, returns JWT token |

### ✅ Tasks

| Method | Endpoint       | Description                |
|--------|----------------|----------------------------|
| GET    | `/tasks`       | List all tasks of the user |
| POST   | `/tasks`       | Create a new task          |
| GET    | `/tasks/{id}`  | Get a single task by ID    |
| PUT    | `/tasks/{id}`  | Update task by ID          |
| DELETE | `/tasks/{id}`  | Delete task by ID          |

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/theMirmakhmudov/FastAPI-Task-JWT.git
cd FastAPI-Task-JWT
```

### 2. Create virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

Now open:

- Swagger Docs: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc

---

## 🛠 Tech Stack

- **FastAPI** — High-performance Python web framework
- **SQLAlchemy** — ORM for working with databases
- **JWT** — Secure user authentication
- **Pydantic** — Data validation and parsing
- **Uvicorn** — Lightweight ASGI server
- **SQLite** — Simple database for development (can be replaced)

---

## 🧪 Testing

To run tests:

```bash
pytest
```

You can add test cases in the `tests/` directory.

---

## 🔐 Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Use `python-dotenv` to load these variables automatically.

---

## 📦 Deployment

You can deploy using:

- Docker
- Gunicorn + Uvicorn
- Systemd
- GitHub Actions (CD example available)

Example systemd service (`fastapi-task.service`):

```ini
[Unit]
Description=FastAPI Task App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/fastapi-task
ExecStart=/home/ubuntu/fastapi-task/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss your ideas.

---

## 📬 Contact

Created by [@theMirmakhmudov](https://github.com/theMirmakhmudov)

---

### ℹ️ Eslatma:
Agar sizda **CI/CD workflow** fayli `ci.yml` deb nomlanmagan bo‘lsa, badge'ni quyidagiga mos ravishda sozlang:
```
https://img.shields.io/github/actions/workflow/status/USERNAME/REPO_NAME/YOUR_WORKFLOW_FILE.yml?label=CI
```

Agar xohlasangiz, siz uchun Dockerfile badge yoki test coverage badge (Codecov/coveralls) ham qo‘shib berishim mumkin. Yana nima qo‘shishni istaysiz?