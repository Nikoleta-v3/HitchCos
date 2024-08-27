"""
Listwiz sorting
---------------

This submodule contains implementations for different sorting methods.


"""


def merge_sort(l):
    """Use the merge sort algorithm to sort the list elements.

    Parameters
    ----------
    l : list
       The list to sort

    Returns
    -------
    sorted_list
    """
    # If there is a single item, the list is already sorted, return.
    if len(l) == 1:
        return l

    split = len(l) // 2
    # Split and sort each part by calling merge_sort recursively
    part1 = merge_sort(l[:split])
    part2 = merge_sort(l[split:])

    # The result is a new list adding always the smaller items from each list
    res = []
    while len(part1) and len(part2):
        if part1[0] <= part2[0]:
            res.append(part1.pop(0))
        else:
            res.append(part2.pop(0))

    # One of the lists is not fully consumed, add all remaining elements:
    if len(part1):
        res.extend(part1)
    else:
        res.extend(part2)

    return res


def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selection_sort(l):
    # We should provide selection sort.
    raise NotImplementedError

