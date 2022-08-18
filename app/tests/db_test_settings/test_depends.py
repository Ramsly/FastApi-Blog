from main import app

from app.depends import get_db
from app.tests.db_test_settings.db_test_settings import TestingSessionLocal


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db