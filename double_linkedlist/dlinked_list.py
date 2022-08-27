from nodes.node import Node
from typing import TypeVar

T = TypeVar('T')


class DoubleLinkedlist(object):
    def __init__(self):
        self.head: Node = Node(None)
        self.tail: Node = Node(None)
        self.head.set_next_pointer(self.tail)
        self.tail.set_previous_pointer(self.head)
        self.count = 0

    def push(self, item: T) -> None:
        new_node = Node(item)
        new_node.set_previous_pointer(self.head)
        new_node.set_next_pointer(self.head.get_next_pointer())
        self.head.get_next_pointer().set_previous_pointer(new_node)
        self.head.set_next_pointer(new_node)
        self.count +=1

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        return self.tail

    def append(self, item) -> None:
        new_node = Node(item)
        new_node.set_next_pointer(self.tail)
        new_node.set_previous_pointer(self.tail.get_previous_pointer())
        self.tail.get_previous_pointer().set_next_pointer(new_node)
        self.tail.set_previous_pointer(new_node)
        self.count +=1

    def delete_item(self, item):
        current = self.head
        while current.get_next_pointer() is not None:
            if current.get_item() == item:
                current.get_previous_pointer().set_next_pointer(current.get_next_pointer())
                current.get_next_pointer().set_previous_pointer(current.get_previous_pointer())
                self.count -=1
                break

            current = current.get_next_pointer()

    def insert_item_at_position(self, position: int, value):
        current = self.head
        new_item = Node(value)
        result = False
        if position <= self.count:
            while current.get_next_pointer() is not None and not result:
                if self.count == position:
                    new_item.set_next_pointer(current.get_next_pointer())
                    new_item.set_previous_pointer(current)
                    current.set_next_pointer(new_item)
                    current.get_next_pointer().set_previous_pointer(new_item)
                    result = True
                    self.count += 1
                current = current.get_next_pointer()

        return result
