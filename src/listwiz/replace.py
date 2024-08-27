"""
Listwiz replace
---------------

This module contains functions to replace some elements of a list.



"""



def replace_sublist(l, sublist, replacement):
    """Naive function to replace a sublist with a replacement list.

    Parameters
    ----------
    l : list
        List to replace all occurances of sublist.
    sublist : list
        A (shorter) list to search for.
    replacement : list
        A new list to insert instead of sublist.

    Examples
    --------
    >>> from listwiz.replace import replace_sublist

    Replace any occurance of ``[2, 3]`` with ``[3, 2]``

    >>> replace_sublist([1, 2, 3, 4], [2, 3], [3, 2])
    [1, 3, 2, 4]

    """
    len_sublist = len(sublist)
    result = l[:]  # copy the input list

    i = 0
    while i < len(result):
        if result[i:i+len_sublist] == sublist:
            result[i:i+len_sublist] = replacement
            i += len_sublist
        else:
            i += 1

    return result


def replace_elements( l, replacements ):
    """Function to replace elements of a list.

    Parameters
    ----------
    l : list
        List to change.
    replacements : dict
        Dictionary of replacements.
    
    Examples
    --------
    >>> from listwiz.replace import replace_elements

    Replace all 2s with 20 and all 3 with 30.

    >>> replace_elements([1, 2, 3], {2: 20, 3: 30})
    [1, 20, 30]

    """
    out = []

    for i in l:
        if i in replacements:
            out.append(replacements[i])
        else:
            out.append(i)
    
    return out
