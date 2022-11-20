import time


class context_manager:
    def __init__(self):
        pass

    def __enter__(self):
        self.__start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("context manager lived {} sec.".format(time.time() - self.__start_time))


if __name__ == "__main__":
    with context_manager() as cm:
        
        time.sleep(1)
        for i in range(1000):
            j = i + 1
