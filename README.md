# Dataset Management API

FastAPI CRUD API. SQLite is used locally; set `DATABASE_URL` to a hosted PostgreSQL connection string for Vercel.

## Local setup (PowerShell)
```powershell
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000/docs.


