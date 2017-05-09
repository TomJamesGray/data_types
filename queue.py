"""
Basic implementation of a queue in python
"""
class Queue(object):
    def __init__(self,initial):
        self.head = QueueVal(initial)
        self.tail = None

    def enqueue(self,data):
        if self.tail == None:
            self.tail = QueueVal(data)
            self.tail.before = self.head
            self.head.after = self.tail
        else:
            tmp = QueueVal(data)
            self.tail.after = tmp
            self.tail = tmp

    def get(self):
        tmp = self.head
        val = tmp.data
        self.head = tmp.after
        return val

class QueueVal(object):
    def __init__(self,data):
        self.data = data
        self.before = None
        self.after = None

if __name__ == "__main__":
    q = Queue("1st")
    q.enqueue("2nd")
    q.enqueue("3rd")
    print(q.get())
    print(q.get())
    print(q.get())

