import os.path as osp
import tempfile

from path import Path

from tf_scribe.cli import collect_git_data

def test_collect_git_data_local():
    git_data = collect_git_data()
    assert git_data['commit'] != "[unknown]"
    assert git_data['repository'] != "[unknown]"

def test_collect_git_data_no_repo():
    with tempfile.NamedTemporaryFile() as f:  # Make a temp dir
        with Path(osp.dirname(f.name)):  # Temporarily cd into our temp dir
            git_data = collect_git_data()
            assert git_data['commit'] == "[unknown]"
            assert git_data['repository'] == "[unknown]"
