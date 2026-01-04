from fastapi import FastAPI
from app.routes.habits import router as habit_router
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Habit Tracker API")

app.include_router(habit_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
