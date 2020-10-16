#!/usr/bin/python3
import urllib.request

"""
fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:$")
        print("\t- type: {}".format(type(respose)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(r.decode('utf-8')))
