#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = [0]
    for key in keys:
        for i in boxes[key]:
            if i < len(boxes):
                if i not in keys:
                    keys.append(i)
    if len(keys) != len(boxes):
        return False
    return True
'''
        if boxes[key] != -999:
            keys += boxes[key]
            boxes[key] = -999

    for i in boxes:
        if i != -999:
            return False
    return True
'''
