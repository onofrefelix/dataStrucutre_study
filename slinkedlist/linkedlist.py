from typing import List, Optional, TypeVar
from nodes.node import Node

T = TypeVar('T')


class LinkedList(object):
    def __init__(self, contents: List[T] = []) -> None:
        self.__first: Node = Node()
        self.__last = self.__first
        self.__count = 0
        for content in contents:
            self.append(content)

    def __len__(self):
        return self.__count

    def getFirst(self) -> Node:
        return self.__first

    def append(self, item: T) -> None:
        node = Node(item)
        self.__last.set_next_pointer(node)
        self.__last = node
        self.__count += 1

    def __getitem__(self, index: int) -> T:
        if 0 <= index < self.__count:
            cursor = self.__first.get_next_pointer()
            for i in range(index):
                cursor = cursor.get_next_pointer()
            return cursor.getItem()
        raise IndexError(f"Index -> {index} Out of Range")

    def __setitem__(self, index: int, item: T) -> None:
        if 0 <= index < self.__count:
            cursor = self.__first.get_next_pointer()
            for i in range(index):
                cursor = cursor.get_next_pointer()
            cursor.setItem(item)

            return
        raise IndexError(f"Index -> {index} Out of Range")

    def insert(self, index: int, item: T) -> None:
        cursor = self.__first
        if index < self.__count:
            for i in range(index):
                cursor = cursor.get_next_pointer()
            node = Node(item)
            node.set_next_pointer(cursor.get_next_pointer())
            cursor.set_next_pointer(node)
        else:
            self.append(item)

    def _add__(self, other):
        if type(self) != type(other):
            raise TypeError("Concatenate undefined for " + str(type(self)) + " + " + str(type(other)))

        result = LinkedList()
        cursor = self.__first.get_next_pointer()
        while cursor is not None:
            result.append(cursor.getItem())
            cursor = cursor.get_next_pointer

        cursor = other.getFirst().getNext()
        while cursor is not None:
            result.append(cursor.getItem())
            cursor = cursor.get_next_pointer()
        return result
