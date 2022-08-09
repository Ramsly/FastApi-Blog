from sqlalchemy.orm import Session

from ..models import Comment
from ..utility_db import add_db_data
from ...exceptions import check_item_exist


def create_comment(db: Session, user_id: int, post_id: int, content: str) -> Comment:
    db_comment = Comment(user_id=user_id, post_id=post_id, content=content)
    return add_db_data(db, db_comment)


def get_comments(db: Session) -> list[Comment] | None:
    return db.query(Comment).all()


def get_comment(db: Session, comment_id: int) -> Comment | None:
    return db.query(Comment).where(comment_id == Comment.id).first()


def update_comment(db: Session, comment_id: int, content: str) -> Comment:
    db_comment = get_comment(db, comment_id)
    check_item_exist(db_comment)
    db_comment.content = content
    return add_db_data(db, db_comment)


def delete_comment(db: Session, comment_id: int) -> None:
    db_comment = get_comment(db, comment_id)
    check_item_exist(db_comment)
    db.delete(db_comment)
    db.commit()