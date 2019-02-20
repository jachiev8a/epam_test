
from validator import validate_xml
from validator import XMLSyntaxError
import pytest
import os


def get_resources_path():
    path = os.path.normpath(
        os.path.dirname(__file__) + os.sep + '_resources')
    return path


def test_good_input():
    """These tests should pass
    """
    assert validate_xml(get_resources_path()+'/valid.xml') is None
    assert validate_xml(get_resources_path()+'/invalid_version.xml') is None


def test_bad_input():

    with pytest.raises(IOError):
        validate_xml('_resources/not_existing.xml')

    with pytest.raises(XMLSyntaxError):
        validate_xml(get_resources_path()+'/empty.txt')

    with pytest.raises(XMLSyntaxError):
        validate_xml(get_resources_path()+'/invalid.xml')
