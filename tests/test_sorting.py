import pytest

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
    # Stub for a test with empty lists
    pass


def test_bubble_sort():
    # Stub for basic bubble sort tests
    pass


def test_selection_sort():
    # Stub for basic selection sort tets
    pass
