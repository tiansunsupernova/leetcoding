from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foolock = Lock()
        self.barlock = Lock()
        self.barlock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.foolock:
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
            self.foolock.acquire()
            self.barlock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.barlock:
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
            self.foolock.release()
            self.barlock.acquire()