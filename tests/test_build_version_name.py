
from validator import build_version_name
import pytest


def test_good_input():
    """These tests should pass
    """
    assert build_version_name(
        'HELLO', 'BRANCH') == 'ci_HELLO_BRANCH_SNAPSHOT'

    assert build_version_name(
        'GiThUb_OrGaNiSaTioN',
        'My_git_BRanch') == 'ci_GiThUb_OrGaNiSaTioN_My_git_BRanch_SNAPSHOT'

    assert build_version_name(
        'HI THERE', 'MY BRANCH') == 'ci_HI THERE_MY BRANCH_SNAPSHOT'


def test_bad_input():
    """These tests should pass with invalid arguments
    """
    with pytest.raises(Exception):
        build_version_name(1, 2)

    with pytest.raises(Exception):
        build_version_name([1,2], -2)

    with pytest.raises(Exception):
        build_version_name(["HELLO"], ["WORLD"])
