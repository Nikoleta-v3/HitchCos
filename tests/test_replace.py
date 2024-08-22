import pytest  # noqa: F401

from listwiz import replace as lwr  # noqa: F401


def test_replace_elements():
    # Stub to be replaced with actual tests when implementing the function,
    # see issue #12.
    pass


def test_replace_sublist_simple():
    # Replace sublist does not have any test right now. See issue #13.
    pass


def test_replace_sublist_overlap():
    # The sublist may match with overlap (e.g. if it is just [1, 1])
    # We should add one or more test that check we replace the first occurance.
    # See issue #13.
    pass


def test_replace_sublist_empty():
    # This is a stub for testing the bug with empty sublists.
    pass
