#!/usr/bin/python3

"""
fetches https://intranet.hbtn.io/status
"""

import request

if __name__ == "__main__":
        response = requests.get("https://intranet.hbtn.io/status")
        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
