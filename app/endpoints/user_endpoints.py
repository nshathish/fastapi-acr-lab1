from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

router = APIRouter()

# In-memory user store
users_db: Dict[int, dict] = {}
user_id_counter = 1

class User(BaseModel):
    id: int
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str

@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = user.model_dump()
    user_data["id"] = user_id_counter
    users_db[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

@router.get("/users/", response_model=List[User])
def list_users():
    return list(users_db.values())

@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user