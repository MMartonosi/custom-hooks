
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
    print("working direcory>>", os.getcwd())
    git_config_file = os.path.join(os.getcwd(), ".git", "config")
    with open(git_config_file) as f:
        data = f.read()
        print(data)
    retval = 0

    retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
