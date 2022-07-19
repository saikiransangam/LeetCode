
from Node import Node
class LinkedList:

    def __init__(self, data):

        self.head_node = None #pointer to first node


    def get_head(self):

        return self.head_node

    def insert_at_tail(self,data):

        return data

    def is_empty(self):

        if self.head_node is None:

            return True

        else:

            return False

