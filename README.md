# Portfolio Dashboard

Modular and extensible dashboard for tracking portfolios, analyzing data, and running optimizations.

## Architecture
- **Frontend:** Next.js (React) with TailwindCSS
- **Backend:** FastAPI (Python) with PostgreSQL and Redis
- **Analytics:** Risk metrics, correlations, efficient frontier via PyPortfolioOpt
- **Charts:** Recharts, Plotly.js, D3.js
- **Deployment:** Docker and docker-compose

## Getting Started
1. Copy `.env.example` to `.env` and fill in credentials.
2. Build and run all services:
   ```bash
   docker-compose up --build
   ```
3. Frontend available at `http://localhost:3000`
4. Backend API available at `http://localhost:8000/api/holdings`
5. Analytics endpoint at `http://localhost:8000/api/analytics`
6. Optimization endpoint at `http://localhost:8000/api/optimization`

## Testing

Run backend and frontend tests after changes:

```bash
python -m pytest
npm --prefix frontend test
```

## Project Structure
```
backend/    # FastAPI application and ingestion stubs
frontend/   # Next.js dashboard UI
```

IBKR connectivity is represented with mock data in `backend/app/ibkr.py`. Replace with real API calls and add analytics or optimization logic as needed.
