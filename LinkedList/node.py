"""https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python"""
class Node:
    """By default data will be None unless explicitly set"""
    def __init__(self, size=0, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = next_next
