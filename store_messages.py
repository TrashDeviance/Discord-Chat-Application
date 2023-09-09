
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append new data to the linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Method to prepend data to the linked list
    def prepend(self, before_head):
        new_node = Node(before_head)
        new_node.next = self.head
        self.head = new_node

    # Method to insert data at a specific index
    def insert(self, index, value):
        pass

    # Method used to display the current data in the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Creating new instance of the LinkedList class
linked_list_store_messages = LinkedList()

