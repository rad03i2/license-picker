import json

from license_picker.cli import main


def test_list_json(capsys):
    assert main(["list", "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert any(item["id"] == "mit" for item in payload)


def test_pick_patent_and_no_copyleft(capsys):
    assert main(["pick", "--patent-grant", "--copyleft", "none", "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert [item["id"] for item in payload] == ["apache-2.0"]


def test_show_unknown_returns_usage_error(capsys):
    assert main(["show", "unknown"]) == 2
    assert "unknown license" in capsys.readouterr().err


def test_compare_human_output(capsys):
    assert main(["compare", "mit", "mpl-2.0"]) == 0
    output = capsys.readouterr().out
    assert "MIT License" in output
    assert "Mozilla Public License 2.0" in output
