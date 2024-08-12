import pytest

from listwiz import sorting as lws


@pytest.mark.xfail(reaso="mergesort doesn't work yet!")
def test_mergesort():
   l = [3, 2, 1, 5, 4, 6]
   res = lws.merge_sort(l)
   assert res == [1, 2, 3, 4, 5, 6]


@pytest.mark.skip(reason="Just a stub, not implemented yet")
def test_bubble_sort():
    pass


@pytest.mark.skip(reason="Just a stub, not implemented yet")
def test_selection_sort():
    pass
