#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line
    data = 50000 * data
    print data
