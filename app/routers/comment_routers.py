from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from ..depends import get_db
from ..schemas.comment_schemes import RequestCommentSchema, ResponseCommentSchema
from ..db.crud.comment_cruds import get_comment, get_comments, create_comment, delete_comment, update_comment
from ..db.database import Base, engine

Base.metadata.create_all(engine)

router = APIRouter(
    prefix="/comments",
    tags=['Comment']
)


@router.get('/', response_model=list[ResponseCommentSchema])
async def get_all_likes(db: Session = Depends(get_db)):
    return get_comments(db)


@router.get('/{comment_id}', response_model=ResponseCommentSchema)
async def get_one_like(comment_id: int = Path(default=None, gt=0, description="Get comment by ID"),
                       db: Session = Depends(get_db)):
    return get_comment(db, comment_id)


@router.post('/create-comment', response_model=ResponseCommentSchema)
async def create_one_like(comment: RequestCommentSchema, db: Session = Depends(get_db)):
    return create_comment(db, comment=comment)


@router.put('/update-comment/{comment_id}', response_model=ResponseCommentSchema)
async def update_one_like(comment: RequestCommentSchema,
                          comment_id: int = Path(default=None, gt=0, description="Update comment by ID"),
                          db: Session = Depends(get_db)):
    return update_comment(db, comment_id=comment_id, content=comment.content)


@router.delete('/delete-comment/{comment_id}', response_model=ResponseCommentSchema)
async def delete_one_like(comment_id: int = Path(default=None, gt=0, description="Delete comment by ID"),
                          db: Session = Depends(get_db)):
    return delete_comment(db, comment_id=comment_id)