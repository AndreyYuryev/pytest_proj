import pytest

from utils import dicts


@pytest.fixture()
def filled_collection():
    return {"vcs": "mercurial"}


@pytest.fixture()
def empty_collection():
    return {}


def test_get_val(filled_collection, empty_collection):
    assert dicts.get_val(filled_collection, 'vcs') == 'mercurial'
    assert dicts.get_val(filled_collection, "vcs", "git") == 'mercurial'
    assert dicts.get_val(empty_collection, "vcs", "git") == 'git'
    assert dicts.get_val(empty_collection, "vcs", "bazaar") == 'bazaar'
