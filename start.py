#!/usr/bin/env python3
import sys


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Success")
        sys.exit(0)
    else:
        print("Fail")
        sys.exit(1)