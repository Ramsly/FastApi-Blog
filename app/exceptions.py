from fastapi.exceptions import HTTPException

from .db.database import Base


def check_item_exist(item: Base) -> None:
    """
    Check if item exist in database.

    :param Base item: Gotten classes instance of Base
    :return: None
    :rtype: None
    """
    if not item:
        raise HTTPException(
            detail='Item does not exist',
            status_code=404
        )