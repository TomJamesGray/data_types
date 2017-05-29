class Graph(object):
    def __init__(self):
        self.nodes = []

    def add_node(self,neighbours):
        tmp = Node(neighbours,len(self.nodes))
        self.nodes.append(tmp)

class Node(object):
    def __init__(self,neighbours,uid):
        self.neighbours = neighbours
        self.uid = uid
        self.arcs = []
        for n in neighbours:
            self.arcs.append(Arc(self,n,1))
    def __repr__(self):
        return "Node object. Neighbours: {}, uid: {}".format(self.neighbours,self.uid)

class Arc(object):
    def __init__(self,n1,n2,weight):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

if __name__ == "__main__":
    g = Graph()
    g.add_node([])
    g.add_node([0])
    g.add_node([0,1])

    print(g.nodes)
