#!/bin/python3

import sys

S = input().strip()

try:
    a = int(S)
    print(a)
except ValueError:
    print("Bad String")
except: #  to serve as a wildcard,  re-raise the exception (allowing a caller to handle the exception as well)
    print("Unexpected error:", sys.exc_info()[0])
    raise