import os
from typing import Generator

import pytest

from learning_pytest.main import Application, get_app

@pytest.fixture(scope="session")
def test_application() -> Application:
    return get_app()

@pytest.fixture(autouse=True)
def cleanup() -> Generator[None, None, None]:
    yield
    if os.path.exists("test.csv"):
        os.remove("test.csv")