"""
A class named SortedList, derived from built-in list, in a module named sorted_list.

Methods are overridden to make sure that the contents of a SortedList are always sorted in
ascending order after any operation.
"""

__author__ = 'Karen Corscadden, a Cabrillo student for CS 12P, kmcorscadden@jeff.cis.cabrillo.edu'


class SortedList(list):
    """
    A Class that stores an always sorted list.
    """
    def __init__(self, *args):
        super().__init__(*args)
        super().sort()

    def __repr__(self):
        if __name__ == '__main__':
            return f'SortedList({super().__repr__()})'
        else:
            return f'{__name__}.SortedList({super().__repr__()})'

    def __add__(self, other):
        x = SortedList(super().__add__(other))
        super(SortedList, x).sort()
        return x

    def __mul__(self, other):
        x = SortedList(super().__mul__(other))
        super(SortedList, x).sort()
        return x

    def __iadd__(self, other):
        super().__iadd__(other)
        super().sort()
        return self

    def __imul__(self, other):
        super().__imul__(other)
        super().sort()
        return self

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().sort()
        return self

    def __reversed__(self):
        pass

    def __str__(self):
        return super().__repr__()

    def append(self, x):
        super().append(x)
        super().sort()

    def extend(self, x):
        super().extend(x)
        super().sort()

    def insert(self, i, x):
        super().insert(i, x)
        super().sort()

    def reverse(self):
        pass

    def sort(self):
        pass
