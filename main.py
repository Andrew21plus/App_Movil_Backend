# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth import router as auth_router
from api.tasks import router as task_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto para producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api", tags=["Auth"])
app.include_router(task_router, prefix="/api", tags=["Tasks"])

@app.get("/")
def read_root():
    return {"message": "Backend funcionando"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}