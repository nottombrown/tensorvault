from tf_scribe.cli import collect_git_data

def test_collect_git_data():
    git_data = collect_git_data()
    assert git_data['commit'] == "[unknown]"
