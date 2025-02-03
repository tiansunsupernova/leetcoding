from threading import Semaphore, Barrier
class H2O:
    def __init__(self):
        self.o_sem = Semaphore(1)
        self.h_sem = Semaphore(2)
        self.water_barrier = Barrier(3)
        pass


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h_sem:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self.water_barrier.wait()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o_sem:
            releaseOxygen()
            self.water_barrier.wait()