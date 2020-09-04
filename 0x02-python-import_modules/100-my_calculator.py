#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def main():
    args, arg_len = sys.argv, len(sys.argv) - 1
    table = {"+": add, "-": sub, "*": mul, "/": div}
    if arg_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, op, b = int(args[1]), args[2], int(args[3])
    c = table[args[2]](a, b)
    print("{} {} {} = {}".format(a, op, b, c))
'''
#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

def main():
    arguments = sys.argv
    agruments = arguments[1:]

    if len(arguments) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif arguments[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a, op, b = int(arguments[1]), arguments[2], int(arguments[3])
    table = {"+": add, "-": sub, "*": mul, "/": div}
    c = table[arguments[2]](a, b)
    print("{} {} {} = {}".format(a, op, b, c))

    elif arguments[2] == "+":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(add(int(arguments[1]), int(arguments[3])))))

    elif arguments[2] == "-":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(sub(int(arguments[1]), int(arguments[3])))))

    elif arguments[2] == "*":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(mul(int(arguments[1]), int(arguments[3])))))

    elif arguments[2] == "/":
        print('{} {} {} = {}'.format(arguments[1], arguments[2], arguments[3], format(div(int(arguments[1]), int(arguments[3])))))
    '''

if __name__ == '__main__':
    main()
