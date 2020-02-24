import threading
from functools import wraps

def reader(f):
    return ReaderWriter.reader(f)

def writer(f):
    return ReaderWriter.writer(f)

class ReaderWriter:

    _r_count, _w_count = 0, 0
    _rmutex, _wmutex = threading.Lock(), threading.Lock()
    _readTry, _rw_mutex = threading.Lock(), threading.Lock()

    @classmethod
    def reader(cls, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # before
            with cls._readTry:
                with cls._rmutex:
                    cls._r_count += 1
                    if (cls._r_count == 1):
                        cls._rw_mutex.acquire()

            o = f(*args, **kwargs)

            # after
            with cls._rmutex:
                cls._r_count -= 1
                if (cls._r_count == 0):
                    cls._rw_mutex.release()

            return o
        return decorated

    @classmethod
    def writer(cls, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            # before
            with cls._wmutex:
                cls._w_count += 1
                if (cls._w_count == 1):
                    cls._readTry.acquire()

            with cls._rw_mutex:
                f(*args, **kwargs)

            # after
            with cls._wmutex:
                cls._w_count -= 1
                if (cls._w_count == 0):
                    cls._readTry.release()
            
            return None
        return decorated
