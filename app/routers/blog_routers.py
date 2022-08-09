from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..depends import get_db
from ..schemas.blog_schemes import RequestBlogScheme, ResponseBlogScheme
from ..db.crud.blog_cruds import get_blog, get_blogs, create_blog, delete_blog, update_blog
from ..db.database import Base, engine


Base.metadata.create_all(engine)

router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)


@router.post('/create', response_model=ResponseBlogScheme)
async def create_blog_router(data: RequestBlogScheme, db: Session = Depends(get_db)):
    return create_blog(db, content=data.content, title=data.title)


@router.get('/all', response_model=list[ResponseBlogScheme])
async def get_all_blogs(db: Session = Depends(get_db)):
    return get_blogs(db)


@router.get('/get/{blog_id}', response_model=ResponseBlogScheme)
async def get_one_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = get_blog(db, blog_id)
    if not blog:
        raise HTTPException(detail='Blog was not found', status_code=404)
