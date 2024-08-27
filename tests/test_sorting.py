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
    # Stub for a test with empty lists, see issue #8
    pass


def test_bubble_sort():
    # Test even-sized list:
    l = [3, 2, 1, 5, 4, 6]
    res = lws.bubble_sort(l)
    assert res == [1, 2, 3, 4, 5, 6]

    # Test odd-sized list:
    l = [5, 4, 3, 2, 1]
    res = lws.bubble_sort(l)
    assert res == [1, 2, 3, 4, 5]

    # Test already sorted list:
    l = [1, 2, 3, 4, 5]
    res = lws.bubble_sort(l)
    assert res == [1, 2, 3, 4, 5]

    # Test list with duplicate elements:
    l = [4, 2, 3, 2, 1, 3]
    res = lws.bubble_sort(l)
    assert res == [1, 2, 2, 3, 3, 4]

    # Test list with all identical elements:
    l = [7, 7, 7, 7]
    res = lws.bubble_sort(l)
    assert res == [7, 7, 7, 7]

    # Test empty list:
    l = []
    res = lws.bubble_sort(l)
    assert res == []

    # Test single-element list:
    l = [1]
    res = lws.bubble_sort(l)
    assert res == [1]


def test_selection_sort():
    # Stub for basic selection sort tests, see issue #10
    pass
