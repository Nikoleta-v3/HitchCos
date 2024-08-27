import pytest  # noqa: F401

from listwiz import sorting as lws


def test_mergesort():
    # Test even sized list:
    l = [3, 2, 1, 5, 4, 6]
    res = lws.merge_sort(l)
    assert res == [1, 2, 3, 4, 5, 6]

    # Test odd sized list:
    l = [5, 4, 3, 2, 1]
    res = lws.merge_sort(l)
    assert res == [1, 2, 3, 4, 5]


def test_mergesort_empty():
    # Test with empty list:
    l = []
    res = lws.merge_sort(l)
    assert res == []

def test_bubble_sort():
    # Stub for basic bubble sort tests, see issue #9
    pass


def test_selection_sort():
    # Stub for basic selection sort tests, see issue #10
    pass
