"""
File: arrays.py
An Array is like a lis, but the client can use only [],
len, iter, and str.

To instantiate, use <variable> = Array(<capacity>, <optional fill values>)

The fill value is None by default.

"""


class Array(object):
    """ Represents an Array."""

    def __init__(self, capacity: int = 0, fillvalue=None) -> None:
        """
        Capacity is the static size of the array.
        fillvalue is palced at each position.

        :param capacity: int
        :param fillvalue: value that will be stored
        """
        self.items = []
        self.count = 0
        for count in range(capacity):
            self.items.append(fillvalue)
            self.count += 1

    def __len__(self):
        """ The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """ The String of representation of the array. """
        return str(self.items)

    def __iter__(self):
        """ Support traversal with for loops"""
        return iter(self.items)

    def __getitem__(self, index: int):
        """ Subscript operator for access at index"""
        if index < len(self.items):
            return self.items[index]
        else:
            raise ValueError(f'index -> {index} out of range')

    def __setitem__(self, index: int, new_item):
        """ Subscript operator for replacement at index."""
        if index < len(self.items):
            self.items[index] = new_item
        else:
            raise ValueError(f'index -> {index} out of range')

    def append(self, item):
        self.items.append(item)
        self.items += 1

    def insertArray(self, array_class):
        self.items += array_class.items
        self.count = len(self.items)


if __name__ == "__main__":
    arr = Array(1)
    a = Array()
    a.insertArray(arr)
