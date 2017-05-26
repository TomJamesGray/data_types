"""
Basic implementation of a linked list in python
"""

class Linked_List(object):
    def __init__(self,initial_data):
        if hasattr(initial_data,"__iter__"):
            self.initial = Node(initial_data[0])
            prev = self.initial
            for i in range(1,len(initial_data)):
                prev.next_node = Node(initial_data[i])
                prev = prev.next_node

    def search(self,needle):
        current = self.initial
        while current != None:
            if current.data == needle:
                return current
            current = current.next_node
        return False

    def add_to_end(self,data):
        current = self.initial
        while current.next_node != None:
            current = current.next_node
        current.next_node = Node(data)

    def delete(self,needle):
        current = self.initial
        previous = None
        while current != None:
            if current.data == needle:
                if previous == None:
                    # Handle moving the initial node if you want to delete
                    # the first node
                    tmp = self.initial
                    self.initial = self.initial.next_node
                    del tmp
                else:
                    current.delete_node(previous)
            previous = current
            current = current.next_node
        return False

    def __repr__(self):
        out = "Linked List: ["
        current = self.initial
        while current != None:
            out += "{} ,".format(current.data)
            current = current.next_node
        return "{}]".format(out[:-2])

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next_node= None

    def __repr__(self):
        return "Node object data: {}".format(self.data)

if __name__ == "__main__":
    x = Linked_List([1,2,3,4])
    x.add_to_end(5)
    x.delete(1)
    print(x)

