#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv
    arguments = arguments[1:]
    result=0
    for args in arguments:
        result += int(args)
            
    print('{}'.format(result))

if __name__ == '__main__':
    main()
