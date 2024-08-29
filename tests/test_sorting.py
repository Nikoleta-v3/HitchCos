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

@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([3, 2, 1, 5, 4, 6], [1, 2, 3, 4, 5, 6]),  # Test even-sized list
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Test odd-sized list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Test already sorted list
        ([4, 2, 3, 2, 1, 3], [1, 2, 2, 3, 3, 4]),  # Test list with duplicate elements
        ([7, 7, 7, 7], [7, 7, 7, 7]),  # Test list with all identical elements
        ([], []),  # Test empty list
        ([1], [1]),  # Test single-element list
    ],
)
def test_bubble_sort(input_list, expected):
    res = lws.bubble_sort(input_list)
    assert res == expected


def test_selection_sort():
    # Stub for basic selection sort tests, see issue #10
    pass
