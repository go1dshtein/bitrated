import pytest
import os


@pytest.fixture
def data_dir():
    return os.path.join(os.path.dirname(__file__), 'data')


@pytest.fixture(autouse=True)
def setup_logging():
    from bitrate.config import setup_logging
    setup_logging('DEBUG')
