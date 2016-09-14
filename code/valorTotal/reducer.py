#!/usr/bin/python

import sys

valueTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisValue = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", valueTotal
        oldKey = thisKey;
        valueTotal = 0

    oldKey = thisKey
    valueTotal += float(thisValue)

if oldKey != None:
    print oldKey, "\t", valueTotal
