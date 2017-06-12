
class Queue(object):
    def __init__(self,vals,n=10):
        self.queue = [None for x in range(n)]
        self.head = -1
        self.tail = -1
        for val in vals:
            self.add(val)

    def add(self,val):
        if self.head == -1 and self.tail == -1:
            self.queue[0] = val
            self.head = 0
            self.tail = 0
        elif self.tail == len(self.queue) -1 and self.head != 0:
            print("Wrapping around")
            self.queue[0] = val
            self.tail = 0
        else:
            self.queue[self.tail+1] = val
            self.tail += 1

    def pop(self):
        last = False
        if self.head == self.tail:
            last = True
        elif self.head == -1:
            return False
        tmp = self.queue[self.head]
        self.queue[self.head] = None

        if last:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % len(self.queue)

        return tmp


    def __repr__(self):
        return "{} Head: {}, Tail: {}".format(self.queue,self.head,self.tail)


if __name__ == "__main__":
    queue = Queue(["a","b","c"],4)
    print(queue)
    queue.pop()
    print(queue)
    queue.pop()
    print(queue)
    queue.pop()
    print(queue)
    queue.pop()