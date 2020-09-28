#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = [0]
    for key in keys:
        if boxes[key] != -999:
            keys += boxes[key]
            boxes[key] = -999

    for i in boxes:
        if i != -999:
            return False
    return True
