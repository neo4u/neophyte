import threading

# lock = ReadWriteLock()
# lock.acquire_read()
# # full on read
# lock.release_read()

class ReadWriteLock:
    """ A lock object that allows many simultaneous "read locks", but only one "write lock." """
    def __init__(self):
        self._read_ready = threading.Condition(threading.Lock())
        self._readers = 0

    def acquire_read(self):
        """ Acquire a read lock. Blocks only if a thread has acquired the write lock. """
        self._read_ready.acquire()      # blocks if a write lock was acquired
        try:
            self._readers += 1
        finally:
            self._read_ready.release()

    def release_read(self):
        """ Release a read lock. """
        self._read_ready.acquire()
        try:
            self._readers -= 1
            if not self._readers:
                self._read_ready.notifyAll()
        finally:
            self._read_ready.release()

    def acquire_write(self):
        """ Acquire a write lock. Blocks until there are no acquired read or write locks. """
        self._read_ready.acquire()      # Blocks if a write or read already has this lock
        while self._readers > 0:
            self._read_ready.wait()

    def release_write(self):
        """ Release a write lock. """
        self._read_ready.release()


class ReadWriteLock2:
    def __init__(self):
        self._read_ready = threading.Condition(threading.Lock())
        self._readers = 0

    def acquire_read(self):
        with self._read_ready:
            self._readers += 1

    def release_read(self):
        with self._read_ready:
            self._readers -= 1
            if not self._readers:
                self._read_ready.notify_all()

    def acquire_write(self):
        with self._read_ready:


    def release_write(self):




# https://docs.python.org/3/library/asyncio-sync.html

# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch06s04.html
