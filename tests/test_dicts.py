from utils import dicts


def test_get_val():
    data = {"vcs": "mercurial"}
    assert dicts.get_val(data, 'vcs') == 'mercurial'
    assert dicts.get_val(data, "vcs", "git") == 'mercurial'
    data = {}
    assert dicts.get_val({}, "vcs", "git") == 'git'
    assert dicts.get_val({}, "vcs", "bazaar") == 'bazaar'