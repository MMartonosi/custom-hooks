import argparse
from typing import Optional
from typing import Sequence


def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)

    retval = 0
    print("Error in commit. Returning 1!")
    retval = 1
    return retval


if __name__ == '__main__':
    exit(main())
