from threading import Semaphore

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.cap = capacity
        self.enq_lock = Semaphore(self.cap)
        self.deq_lock = Semaphore(0)
        self.res = deque()

    def enqueue(self, element: int) -> None:
        self.enq_lock.acquire()
        self.res.append(element)
        self.deq_lock.release()

    def dequeue(self) -> int:
        self.deq_lock.acquire()
        x = self.res.popleft() 
        self.enq_lock.release()
        return x

    def size(self) -> int:
        return len(self.res)