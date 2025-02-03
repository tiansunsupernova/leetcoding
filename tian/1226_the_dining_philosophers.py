from threading import Lock
class DiningPhilosophers:
    def __init__(self):
        self.forks = [Lock() for _ in range(5)]

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        if philosopher ^ 1:
            l = (philosopher - 1) % 5
            r = philosopher
        else:
            r = (philosopher - 1) % 5
            l = philosopher
        self.forks[l].acquire()
        self.forks[r].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.forks[l].release()
        self.forks[r].release()
        