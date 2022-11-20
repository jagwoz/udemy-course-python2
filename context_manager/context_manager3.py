import time
from contextlib import contextmanager


class context_manager:
    def __init__(self):
        self.__start_time = time.time()

    def open(self):
        print("context manager opened at {}.".format(time.time()))
        return self

    def close(self):
        print("context manager lived {} sec.".format(time.time() - self.__start_time))


@contextmanager
def cm(obj):
    obj.open()
    yield obj
    obj.close()


if __name__ == "__main__":
    with cm(context_manager()) as cm:
        
        time.sleep(1)
        for i in range(1000):
            j = i + 1
