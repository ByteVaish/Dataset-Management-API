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

## Vercel deployment
1. Push these project files to GitHub. Do not upload virtual environments, `.env`, or database files.
2. Create a hosted PostgreSQL database (for example, Neon) and copy its connection string.
3. Import the GitHub repository at https://vercel.com/new.
4. In Vercel Project Settings → Environment Variables, add `DATABASE_URL` with the PostgreSQL connection string. Apply to Production.
5. Redeploy, then open `https://YOUR-PROJECT.vercel.app/docs`.

Vercel detects the FastAPI `app` in root-level `main.py`; no `vercel.json` is needed for this layout.

## Endpoints
- POST `/datasets/`
- GET `/datasets/`
- GET `/datasets/{dataset_id}`
- PUT `/datasets/{dataset_id}`
- DELETE `/datasets/{dataset_id}`
