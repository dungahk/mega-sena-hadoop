#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) >= 19:
        state = data[len(data) - 10]
        if state != None and state != "" and len(state) == 2:
            print "{0}\t{1}".format(state, 1)
