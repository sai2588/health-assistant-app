
# Health Assistant App

This is a sample project to demonstrate building a **Health Assistant App** using:

- Frontend: React
- Backend: FastAPI
- Database: PostgreSQL (Docker)
- LLM Provider: OpenRouter

## Setup Instructions

### 1. Clone the repo (after you upload this to your GitHub)

### 2. Add `.env` file
In `backend/.env` add:
```
OPENROUTER_API_KEY=your-openrouter-api-key
DATABASE_URL=postgresql+psycopg2://dev-admin:password123@db:5432/health_db
```

### 3. Start the project

```bash
docker-compose up --build
```

- Frontend: [http://localhost:3000](http://localhost:3000)
- Backend: [http://localhost:8000/docs](http://localhost:8000/docs)

### 4. Use the App
Ask health questions and get responses powered by **OpenRouter LLM models**.

## Folder Structure

```
/frontend - React app (user interface)
/backend - FastAPI app (API and database)
/db - PostgreSQL managed via Docker
```

## Important

- **NEVER expose OpenRouter API key to frontend.**
- All AI requests should go through **FastAPI backend**.
- Chat history is saved in PostgreSQL.

## License
MIT
        