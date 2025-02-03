import threading
import time

# -------------------------------
# Lock Example: Mutual Exclusion
# -------------------------------
def lock_example():
    # Create a Lock object to protect the shared resource
    lock = threading.Lock()
    shared_counter = 0

    # Define a function that increments the shared counter
    def increment():
        nonlocal shared_counter
        for _ in range(10000):
            # Using a context manager to acquire/release the lock
            with lock:
                shared_counter += 1

    # Create several threads that will run the increment function
    threads = [threading.Thread(target=increment) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Lock Example - Final Counter Value:", shared_counter)


# --------------------------------------------
# Semaphore Example: Limiting Concurrent Access
# --------------------------------------------
def semaphore_example():
    # Initialize a Semaphore to allow 3 threads concurrently
    sem = threading.Semaphore(3)

    def access_resource(thread_id):
        # Acquire the semaphore (decrements the counter)
        sem.acquire()
        try:
            print(f"Semaphore Example - Thread {thread_id} is accessing the resource")
            time.sleep(1)  # Simulate work with the shared resource
        finally:
            # Release the semaphore (increments the counter)
            print(f"Semaphore Example - Thread {thread_id} is releasing the resource")
            sem.release()

    # Create 5 threads, but only 3 can access the resource at a time
    threads = [threading.Thread(target=access_resource, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# --------------------------------------
# Barrier Example: Thread Synchronization
# --------------------------------------
def barrier_example():
    # Create a Barrier for 3 threads. They will wait until all have reached the barrier.
    barrier = threading.Barrier(3)

    def worker(thread_id):
        print(f"Barrier Example - Thread {thread_id} is performing pre-barrier work")
        time.sleep(thread_id)  # Simulate varying work durations
        print(f"Barrier Example - Thread {thread_id} is waiting at the barrier")
        # Wait at the barrier until all threads have called wait()
        barrier.wait()
        print(f"Barrier Example - Thread {thread_id} passed the barrier")

    # Start three threads
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(1, 4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# ---------------------------------------------------
# Condition Example: Producer-Consumer Synchronization
# ---------------------------------------------------
def condition_example():
    # Create a Condition variable (with an underlying lock)
    condition = threading.Condition()
    shared_list = []
    max_items = 5  # Maximum items the shared_list can hold

    # Consumer thread: Wait until there is at least one item to consume
    def consumer():
        nonlocal shared_list
        with condition:
            while not shared_list:
                print("Condition Example - Consumer waiting for items...")
                condition.wait()  # Releases the lock and waits until notified
            item = shared_list.pop(0)
            print(f"Condition Example - Consumer consumed item: {item}")

    # Producer thread: Produce an item and notify the waiting consumer
    def producer(item):
        nonlocal shared_list
        with condition:
            # If shared_list is full, wait (not demonstrated here for simplicity)
            while len(shared_list) >= max_items:
                condition.wait()
            shared_list.append(item)
            print(f"Condition Example - Producer produced item: {item}")
            condition.notify()  # Wake up one waiting consumer

    # Create producer and consumer threads
    prod_thread = threading.Thread(target=producer, args=(1,))
    cons_thread = threading.Thread(target=consumer)

    cons_thread.start()
    # Give the consumer time to start and wait for items
    time.sleep(0.5)
    prod_thread.start()

    prod_thread.join()
    cons_thread.join()


# -------------------------------
# Main: Run All Examples
# -------------------------------
if __name__ == "__main__":
    print("Starting Lock Example")
    lock_example()

    print("\nStarting Semaphore Example")
    semaphore_example()

    print("\nStarting Barrier Example")
    barrier_example()

    print("\nStarting Condition Example")
    condition_example()
