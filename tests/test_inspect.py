import pytest  # noqa: F401

from listwiz import inspect as lwi  # noqa: F401


@pytest.mark.xfail(reason="the function doesn't work yet")
def test_largest_element():
    l = [1, 2, 100, -1000, 0]

    res_val, res_idx = lwi.largest_element(l)
    assert res_val == 100
    assert res_idx == 2


@pytest.mark.xfail(reason="This function isn't working")
def test_longest_increasing_streak():
    l = [3, 1, 2, 3, 4, -1]

    res_streak, res_pos = lwi.longest_increasing_streak(l)
    assert res_streak == [1, 2, 3, 4]
    assert res_pos == 1


@pytest.mark.skip(reason="Test is not implemented yet")
def test_longest_decreasing_streak():
    raise AssertionError("This test is missing.")



def test_most_common_element():
    ll = [1, 2, 3, 4, 1, 1, 2, 3, 3, 3, 3, 3]
    res = lwi.most_common_element(ll)
    assert res == 3
    
    


#@pytest.mark.skip(reason="Test is not implemented yet")
#def test_most_common_element():
#    raise AssertionError("This test is missing.")

