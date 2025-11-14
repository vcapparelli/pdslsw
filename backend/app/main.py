from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncpg
import os


app = FastAPI()
DATABASE_URL = os.getenv('DATABASE_URL', 'postgres://postgres:password@db:5432/postgres')

# Configurar CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


async def get_pool():
    return await asyncpg.create_pool(DATABASE_URL)


@app.get("/softwares")
async def read_softwares():
    try:
        pool = await get_pool()
        async with pool.acquire() as conn:
            query = "SELECT id, name FROM softwares ORDER BY id"
            rows = await conn.fetch(query)
            return [{"id": r["id"], "name": r["name"]} for r in rows]
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao conectar com o Banco de Dados")
