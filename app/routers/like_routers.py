from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from ..depends import get_db
from ..schemas.likes_shemes import RequestLikesScheme, ResponseLikeScheme
from ..db.crud.like_cruds import get_like, create_likes, delete_like, update_like, get_likes
from ..db.database import Base, engine

Base.metadata.create_all(engine)

router = APIRouter(
    prefix="/likes",
    tags=['Like']
)


@router.get('/', response_model=list[ResponseLikeScheme])
async def get_all_likes(db: Session = Depends(get_db)):
    return get_likes(db)


@router.get('/{like_id}', response_model=ResponseLikeScheme)
async def get_one_like(like_id: int = Path(default=0, ge=0), db: Session = Depends(get_db)):
    return get_like(db, like_id)


@router.post('/create-like', response_model=ResponseLikeScheme)
async def create_one_like(like: RequestLikesScheme, db: Session = Depends(get_db)):
    return create_likes(db, post_id=like.post_id, user_id=like.user_id)


@router.put('/update-like/{like_id}', response_model=ResponseLikeScheme)
async def update_one_like(like_id: int, like: RequestLikesScheme, db: Session = Depends(get_db)):
    return update_like(db, like_id=like_id, post_id=like.post_id, user_id=like.user_id)


@router.delete('/delete-like/{like_id}', response_model=ResponseLikeScheme)
async def delete_one_like(like_id: int, db: Session = Depends(get_db)):
    return delete_like(db, like_id=like_id)