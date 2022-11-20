from contextlib import closing, suppress
from urllib.request import urlopen
import os


if __name__ == "__main__":
    with closing(urlopen("http://www.wp.pl")) as page:
        for line in page:
            # print(line)
            pass

    with suppress(FileNotFoundError):
        os.remove('path/file.txt')
