#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        maxi = list(a_dictionary.keys())[0]
        for key in a_dictionary.keys():
            if a_dictionary[key] > a_dictionary[maxi]:
                maxi = key
        return maxi
    else:
        return None
