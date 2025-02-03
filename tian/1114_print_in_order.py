from threading import Lock

class Foo:
    def __init__(self):
        self.firstlock = Lock()
        self.secondlock = Lock()
        self.firstlock.acquire()
        self.secondlock.acquire()
        pass


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstlock.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        with self.firstlock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
        self.secondlock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.secondlock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()