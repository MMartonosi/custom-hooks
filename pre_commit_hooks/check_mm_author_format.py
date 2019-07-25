
import sys
import os
import argparse
from typing import Optional
from typing import Sequence


def main(argv=None):
    print("Error in commit. Returning 1!")
    # parser = argparse.ArgumentParser()
    # args = parser.parse_args(argv)

    print("---------------------")
    print("new print")
    print(os.path.dirname(os.path.abspath(__file__)))
    retval = 0

    retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
