from fastapi import APIRouter, Depends, Path
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
async def create_one_blog(data: RequestBlogScheme, db: Session = Depends(get_db)):
    return create_blog(db, content=data.content, title=data.title)


@router.get('/all', response_model=list[ResponseBlogScheme])
async def get_all_blogs(db: Session = Depends(get_db)):
    return get_blogs(db)


@router.get('/{blog_id}', response_model=ResponseBlogScheme)
async def get_one_blog(blog_id: int = Path(default=None, gt=0, description="Get blog by ID"),
                       db: Session = Depends(get_db)):
    return get_blog(db, blog_id=blog_id)


@router.put('/{blog_id}', response_model=ResponseBlogScheme)
async def update_one_blog(data: RequestBlogScheme,
                          blog_id: int = Path(default=None, gt=0, description="Update blog by ID"),
                          db: Session = Depends(get_db)):
    return update_blog(db, blog_id=blog_id, title=data.title, content=data.content)


@router.delete('/{blog_id}')
async def delete_one_blog(blog_id: int = Path(default=None, gt=0, description="Delete blog by ID"),
                          db: Session = Depends(get_db)):
    return delete_blog(db, blog_id=blog_id)