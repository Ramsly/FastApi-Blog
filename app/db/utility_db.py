from sqlalchemy.orm import Session

from .database import Base


def add_db_data(db: Session, db_item: Base) -> Base:
    """
    Create a SQLAlchemy model instance with your data.\n
    **Add** that instance object to your database session.\n
    **Commit** the changes to the database (so that they are saved).\n
    **Refresh** your instance (so that it contains any new data from the database, like the generated ID).\n

    :param Session db: Session from SQLAlchemy
    :param Base db_item:
    :return: database item
    :rtype: Base
    """
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item