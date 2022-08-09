from sqlalchemy.orm import Session

from ..models import Like
from ..utility_db import add_db_data
from ...exceptions import check_item_exist


def create_likes(db: Session, post_id: int, user_id: int) -> Like:
    db_like = Like(post_id=post_id, user_id=user_id)
    return add_db_data(db, db_like)


def get_like(db: Session, like_id: int) -> Like | None:
    return db.query(Like).where(Like.id == like_id).first()


def get_likes(db: Session) -> list[Like]:
    return db.query(Like).all()


def update_like(db: Session, like_id: int, post_id: int, user_id: int) -> Like:
    db_like = get_like(db, like_id)
    check_item_exist(db_like)
    db_like.post_id = post_id
    db_like.user_id = user_id
    return add_db_data(db_like)


def delete_like(db: Session, like_id: int) -> None:
    db_like = get_like(db, like_id)
    check_item_exist(db_like)
    db.delete(db_like)
    db.commit()