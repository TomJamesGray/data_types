"""
Basic implementation of a linked list in python
"""

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node= None
    def add_node(self,data_new):
        self.next_node = Node(data_new)
    def __repr__(self):
        return "Node object data: {}".format(self.data)

def search_linked_list(start,needle):
    current = start
    while current != None:
        if current.data == needle:
            return current
        current = current.next_node
    return False

if __name__ == "__main__":
    initial = Node(0)
    current = initial
    # Initialise linked list with data values 0 to 9
    for i in range(1,10):
        current.add_node(i)
        current = current.next_node
        print(i)

    current = initial
    # Go through the linked list until it ends
    while current != None:
        print("Output: {}".format(current))
        current = current.next_node

    print(search_linked_list(initial,5))
    print(search_linked_list(initial,100))
