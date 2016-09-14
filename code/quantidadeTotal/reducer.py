#!/usr/bin/python

import sys

stateTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisState = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", stateTotal
        oldKey = thisKey;
        stateTotal = 0

    oldKey = thisKey
    stateTotal += int(thisState)

if oldKey != None:
    print oldKey, "\t", stateTotal
