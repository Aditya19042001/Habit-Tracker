from pydantic import BaseModel

class HabitCreate(BaseModel):
    name: str

class HabitResponse(BaseModel):
    id: int
    name: str
    is_active: bool

    class Config:
        from_attributes = True
