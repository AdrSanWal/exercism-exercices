"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list1, list2):
    def split(lst, length, lst2, res):
        """Splits 'lst' in  sublists with lenght=length, and check
        if any of them is equal to 'lst2'. If there is a match return 'res'
        else it returns 3.
        Example:
        sublist([0, 1, 2, 3, 1, 2, 5, 6], 3, [2, 5], 0) will return 0
        because [2, 5] in [[0, 1], [1, 2], [2, 3], [3, 1], [1, 2], [2, 5], ...]
        """
        sublst = [lst[a: a + length] for a in range(len(lst) - (length - 1))]
        return res if lst2 in sublst else 3
    if list1 == list2:
        return 2
    len1, len2 = len(list1), len(list2)
    if len1 > len2:
        return split(list1, len2, list2, 1)
    if len2 > len1:
        return split(list2, len1, list1, 0)
    return 3
