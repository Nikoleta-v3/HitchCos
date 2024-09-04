"""
Listwiz inspect
---------------

This module contains some functions inspecting a list.

"""

from collections import Counter


def largest_element(l):
    """Find the largest element and its index

    Parameters
    ----------
    l : list
        The list to find the largest element in.

    Returns
    -------
    value, index :
        A tuple of the largest value and its index.
    """
    # return value, index
    raise NotImplementedError


def longest_increasing_streak(l):
    # It would be nice to have a function to find the
    # longest increasing streak of a list.  E.g.:
    # l = [3, 1, 2, 3, 4, -1] would return:
    # [1, 2, 3, 4] and 1 (where the streak starts).
    raise NotImplementedError


def longest_decreasing_streak(l):
    # It would be nice to have a function to find the
    # longest decreasing streak of a list.  E.g.:
    # l = [-1, -2, 5, 4, 3, 100] would return:
    # [5, 4, 3] and 2 (where the streak starts).
    raise NotImplementedError


def most_common_element(ll):
    """Find the most common element in a list.

    Parameters
    ----------
    ll : list

    Returns
    -------
    most common element
    """
    
    if not isinstance(ll, list):
        raise ValueError("Input must be a list")
    
    c = Counter(ll)
    return c.most_common(1)[0][0]
    