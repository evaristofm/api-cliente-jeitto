import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.exc import IntegrityError

from app.app import app
from app.cli import cliente_create

os.environ["APP_DB__uri"] = "postgresql://postgres:postgres@db:5432/app_test"


@pytest.fixture(scope="function")
def api_client():
    return TestClient(app)


@pytest.fixture(scope="function")
def api_cliente_test():
    return cliente_create("Jhon Doe", "jhondoe@test.com", "81911111111")
