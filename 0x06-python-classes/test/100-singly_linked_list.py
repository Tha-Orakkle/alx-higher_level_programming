#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            return

        while value < self.head.data:
            new_node.next_data = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next_data and temp.next_data.data < value:
            temp = temp.next_node
        new_node.next_node = temp.next_node
        temp.next_node = new_node
