#!/usr/bin/python3
"""
    100-singly_linked_list.py
    Module defining linked lists
    return {}
"""


class Node():
    """A Node class."""

    def __init__(self, data, next_node=None):
        """Initialize class."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve data at Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set value of Node class"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve next Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set value of next Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """A singly linked list class."""

    def __init__(self):
        """Initialize class."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node according to its sorted value."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        curr = self.__head
        while value >= curr.data:
            prev = curr
            if curr.next_node:
                curr = curr.next_node
            else:
                curr.next_node = new_node
                return
        prev.next_node = new_node
        new_node.next_node = curr

    def __str__(self):
        """String representation of class."""
        string = ""
        curr = self.__head
        while curr:
            string += str(curr.data) + "\n"
            curr = curr.next_node
        return string[:-1]
