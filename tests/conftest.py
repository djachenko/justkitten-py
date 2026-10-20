from pathlib import Path

import pytest

pytest_plugins = ["justkitten.testing"]


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    return tmp_path
