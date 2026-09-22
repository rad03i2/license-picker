import pytest

from license_picker import compare, get_license, recommend


def test_get_license_is_case_insensitive():
    assert get_license("MIT").name == "MIT License"


def test_unknown_license_is_rejected():
    with pytest.raises(ValueError, match="unknown license"):
        get_license("made-up")


def test_patent_filter_only_returns_explicit_grants():
    items = recommend(patent_grant=True)
    assert items
    assert all(item.patent_grant for item in items)
    assert {item.id for item in items} >= {"apache-2.0", "gpl-3.0"}


def test_copyleft_filter():
    assert [x.id for x in recommend(copyleft="file")] == ["mpl-2.0"]


def test_notice_filter():
    assert [x.id for x in recommend(notice_required=False)] == ["unlicense"]


def test_compare_deduplicates_preserving_order():
    assert [x.id for x in compare(["mit", "apache-2.0", "mit"])] == ["mit", "apache-2.0"]


def test_compare_requires_input():
    with pytest.raises(ValueError, match="at least one"):
        compare([])
