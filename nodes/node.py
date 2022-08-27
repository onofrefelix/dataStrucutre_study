from typing import TypeVar, Optional

T = TypeVar('T')


class Node(object):
    """ This class represent a singly linked node"""

    def __init__(self, item: Optional[T] = None) -> None:
        """
        Class Constructor
        :param item: Value stored on self._item
        """
        self._item = item
        self._next_pointer = None
        self._previous_pointer = None

    def setItem(self, item: T) -> None:
        """
        Set a new value on a node
        :param item: set new value on Node
        :return: None
        """
        self._item = item

    def get_item(self) -> T:
        """
        :return: return a value stored on a node
        """
        return self._item

    def get_next_pointer(self):
        """
        Return the value of the pointer where there actual Node is pointing
        :return: Point to the next element
        """
        return self._next_pointer

    def get_previous_pointer(self):
        """
        Return the value of the pointer where there actual Node is pointing
        :return: Point to the next element
        """
        return self._previous_pointer

    def set_previous_pointer(self, previous) -> None:
        """
        Return the value of the pointer where there actual Node is pointing
        :return: Point to the next element
        """
        self._previous_pointer = previous

    def set_next_pointer(self, pnext) -> None:
        """

        :param pnext: pointer value which point to the next element
        :return: None
        """
        self._next_pointer = pnext
