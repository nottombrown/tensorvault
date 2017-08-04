from path import Path

from tf_scribe.cli import collect_git_data

def test_collect_git_data_local():
    git_data = collect_git_data()
    assert git_data['commit'] != "[unknown]"
    assert git_data['repository'] != "[unknown]"

def test_collect_git_data_no_repo():
    with Path('/tmp'):
        git_data = collect_git_data()
        assert git_data['commit'] == "[unknown]"
        assert git_data['repository'] == "[unknown]"
