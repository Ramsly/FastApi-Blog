from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..depends import get_db
from ..schemas.user_schemes import RequestUser, ResponseUser
from ..db.crud.user_cruds import get_users, get_user_by_username, create_user, delete_user, update_user
from ..db.database import Base, engine
from ..security import get_current_active_user

Base.metadata.create_all(engine)

router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.post("/create", response_model=ResponseUser)
async def create_one_user(user: RequestUser, db: Session = Depends(get_db)):
    return create_user(db, user=user)


@router.get("/get/{user_username}", response_model=ResponseUser)
async def get_one_user(user_username: str, db: Session = Depends(get_db)):
    return get_user_by_username(db, username=user_username)


@router.get("/me", response_model=ResponseUser)
async def get_current_user(current_user: RequestUser = Depends(get_current_active_user)):
    return current_user


@router.get('/all', response_model=list[ResponseUser])
async def get_all_users(db: Session = Depends(get_db)):
    return get_users(db)


@router.delete('/delete/{user_username}', response_model=ResponseUser)
async def delete_one_user(user_username: str, db: Session = Depends(get_db)):
    return delete_user(db, username=user_username)


@router.put('/update/{user_username}', response_model=ResponseUser)
async def update_one_user(user_username: str, user: RequestUser, db: Session = Depends(get_db)):
    return update_user(db, username=user_username, user=user)