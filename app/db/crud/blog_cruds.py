from sqlalchemy.orm import Session

from ..models import Blog
from ..utility_db import add_db_data
from ...exceptions import check_item_exist


def create_blog(db: Session, content: str, title: str) -> Blog:
    db_blog = Blog(content=content, title=title)
    return add_db_data(db, db_blog)


def get_blogs(db: Session) -> list[Blog]:
    return db.query(Blog).all()


def get_blog(db: Session, blog_id: int) -> Blog | None:
    return db.query(Blog).where(Blog.id == blog_id).first()


def update_blog(db: Session, blog_id: int, title: str, content: str) -> Blog:
    db_blog = get_blog(db, blog_id)
    check_item_exist(db_blog)
    db_blog.title = title
    db_blog.content = content
    return add_db_data(db, db_blog)


def update_blog_visible(db: Session, blog_id: int) -> Blog:
    db_blog = get_blog(db, blog_id)
    check_item_exist(db_blog)
    db_blog.visible = not db_blog.visible
    return add_db_data(db, db_blog)


def delete_blog(db: Session, blog_id: int) -> None:
    db_blog = get_blog(db, blog_id)
    check_item_exist(db_blog)
    db.delete(db_blog)
    db.commit()
