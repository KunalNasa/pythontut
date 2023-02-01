#The Command Line Utilities allows experienced system administrators to perform tasks from the command line prompt
# rather than the graphical user interface.
# example - In terminal: python3 "name of file"
import argparse
import sys


def calc(args):
    if args.o == 'add':
        # if args.x == 5 and args.y == 5:
        #     return 55
        return args.x + args.y
    if args.o == 'sub':
        return args.x - args.y
    if args.o == 'mul':
        return args.x * args.y
    if args.o == 'div':
        return args.x / args.y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help="Enter first number. This is a utility for calculations.Please contact Kunal")
    parser.add_argument('--y', type=float, default=3.0,
                        help="Enter second number. This is a utility for calculations.Please contact Kunal")
    parser.add_argument('--o', type=str, default="add",
                        help="This is a utility for calculations.Please contact Kunal")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    #first change dir to pycharmprojects/pythontut by using cd command and then,
    #write " python3 commandutility.py --x 7 --y 8 --o add " to run in mac terminal.
