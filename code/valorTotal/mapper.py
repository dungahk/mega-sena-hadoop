#!/usr/bin/python

import sys

def valueToFloat(value):
    value = value.replace('.', '')
    value = value.replace(',', '.')
    return float(value)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) >= 19:
        state = data[len(data) - 10]
        value = valueToFloat(data[len(data) - 9])
        if state != None and state != "" and len(state) == 2:
            print "{0}\t{1}".format(state, value)
