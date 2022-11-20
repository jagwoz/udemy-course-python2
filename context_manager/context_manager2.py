from contextlib import redirect_stdout
import time


class context_manager:
    def __init__(self):
        print("context manager initialized at {}".format(time.time()))
        pass

    def __enter__(self):
        print("context manager entered at {}".format(time.time()))
        self.__start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("context manager exited at {}".format(time.time()))
        print("context manager lived {} sec.".format(time.time() - self.__start_time))


if __name__ == "__main__":
    with redirect_stdout(open('log.txt', 'w')):
        with context_manager() as cm:

            time.sleep(1)
            for i in range(1000):
                j = i + 1
