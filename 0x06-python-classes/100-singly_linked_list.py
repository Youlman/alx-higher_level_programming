#!/usr/bin/python3

""" class Node that defines a node of a singly linked list"""


class Node:
    """Represents a Node of syngly linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new node
            Args:
                data: the data
                next_node: the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Set data"""
        if not isinstance(value, int):
            self.__data = value
        raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get next node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Set the next node"""
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


""" A class SinglyLinkeList that defines a singly linked list"""


class SinglyLinkedList:
    """Represent a new single linkde list"""
    def __init__(self):
        "Initialize a new single list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
