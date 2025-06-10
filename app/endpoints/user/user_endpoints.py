from fastapi import APIRouter, HTTPException
from typing import List, Dict

from app.endpoints.user.user_models import User, UserCreate, UserUpdate

router = APIRouter()

# In-memory user store
users_db: Dict[int, dict] = {}
user_id_counter = 1


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


@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user_update.model_dump(exclude_unset=True)
    user.update(update_data)
    users_db[user_id] = user
    return user


@router.delete("/users/{user_id}", response_model=dict)
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"detail": "User deleted"}
