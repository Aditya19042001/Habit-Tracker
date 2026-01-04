from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.habit import Habit
from app.schemas.habit import HabitCreate, HabitResponse

router = APIRouter(prefix="/habits", tags=["habits"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=HabitResponse)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db)):
    db_habit = Habit(name=habit.name)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit
