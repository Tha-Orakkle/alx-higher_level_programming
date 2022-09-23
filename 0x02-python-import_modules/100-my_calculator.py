#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])
    match str(sign):
        case "+":
            print("{} {} {} = {}".format(a, sign, b, add(a, b)))
        case "-":
            print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
        case "*":
            print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
        case "/":
            print("{} {} {} = {}".format(a, sign, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
