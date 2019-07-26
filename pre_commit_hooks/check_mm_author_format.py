
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
    print(os.path.dirname(os.path.abspath(__file__))) # change to this
    print("working direcory>>", os.getcwd()) # from this
    git_config_file = os.path.join(os.getcwd(), ".git", "config")
    with open(git_config_file) as f:
        data = f.read()
        user_data = data.split("[user]")[1]
        user_email = user_data.split("email = ")[1]
        print(user_email)

    retval = 0

    retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
