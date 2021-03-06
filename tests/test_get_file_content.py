
from validator import get_file_content
import pytest
import os


def get_resources_path():
    path = os.path.normpath(
        os.path.dirname(__file__) + os.sep + '_resources')
    return path


def test_good_input():
    """These tests should pass
    """
    assert get_file_content(get_resources_path()+'/valid.xml') == """<project
    xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <modelVersion>4.0.0</modelVersion>
    <groupId>com.wsi.devops</groupId>
    <artifactId>python-test</artifactId>
    <version>1.0-SNAPSHOT</version>
</project>"""

    assert get_file_content(get_resources_path()+'/empty.txt') == ''


def test_bad_input():
    """These tests should pass with invalid arguments
    """
    with pytest.raises(IOError):
        get_file_content('_resources/not_existing_file.txt')
