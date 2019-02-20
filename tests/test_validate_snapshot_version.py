
from validator import validate_snapshot_version
import pytest
import os


def get_resources_path():
    path = os.path.normpath(
        os.path.dirname(__file__) + os.sep + '_resources')
    return path


def test_good_input():
    """These tests should pass
    """
    assert validate_snapshot_version(get_resources_path()+'/valid.xml') is None


def test_bad_input():
    """These tests should pass with invalid arguments
    """
    with pytest.raises(Exception):
        validate_snapshot_version(get_resources_path()+'/invalid_version.xml')
