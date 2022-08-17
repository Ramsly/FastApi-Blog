from sqlalchemy.orm import Session

from ..models import User
from ..utility_db import add_db_data
from ...exceptions import check_item_exist
from ...schemas.user_schemes import RequestUser
from ...security import get_password_hash


def create_user(db: Session, user: RequestUser) -> User:
    db_user = User(username=user.username, email=user.email, password=get_password_hash(password=user.password))
    return add_db_data(db, db_user)


def get_users(db: Session) -> list[User] | None:
    return db.query(User).all()


def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).where(User.username == username).first()


def update_user(db: Session, username: str, user: RequestUser) -> User:
    db_user = get_user_by_username(db, username)
    check_item_exist(db_user)
    db_user.f_name = user.f_name
    db_user.l_name = user.l_name
    db_user.email = user.email
    db_user.username = user.username
    return add_db_data(db, db_user)


def update_disable_user(db: Session, username: str) -> User:
    db_user = get_user_by_username(db, username)
    check_item_exist(db_user)
    db_user.disabled = not db_user.disabled
    return add_db_data(db, db_user)


def delete_user(db: Session, username: str) -> None:
    db_user = get_user_by_username(db, username)
    check_item_exist(db_user)
    db.delete(db_user)
    db.commit()