from __future__ import print_function
from argparse import ArgumentParser
from random import choice, random
from re import match
from Trolls import *
from Nice import *

import sys

if __name__ == '__main__':
    parser = ArgumentParser(description="Brainfuck Console")
    parser.add_argument("-i", "--interpreter",
                        type=str, default="nice",
                        choices=["nice", "reset",
                                 "chars", "file",
                                 "browser", "random"],
                        help="interpreter to use")
    parser.add_argument("-l", "--launch", action='store_true',
                        default=False, help=("whether or not to launch "
                                             "the console when a Brainfuck "
                                             "file or code has been provided"))
    parser.add_argument("-f", "--file", default=None, type=str,
                        help="Brainfuck file to run (optional)")
    parser.add_argument("-c", "--code", default=None, type=str,
                        help="Brainfuck code to run (optional)")
    parser.add_argument("-v", "--version", action='store_true',
                        default=False, help=("Brainfuck interpreter "
                                             "version"))

    args = parser.parse_args()
    interpreter = None
    stdout = False

    if args.version:
        print("Epic Brainfuck 1.0.0")
        sys.exit(0)

    if args.interpreter == "random":
        args.interpreter = choice(["nice", "reset", "chars",
                                   "file", "browser"])

    if args.interpreter == "nice":
        interpreter = NiceInterpreter()

    elif args.interpreter == "reset":
        interpreter = ResetTrollInterpreter()

    elif args.interpreter == "chars":
        interpreter = SetCharsTrollInterpreter()

    elif args.interpreter == "file":
        interpreter = RandomFileTrollInterpreter()

    elif args.interpreter == "browser":
        interpreter = WebbrowserTrollInterpreter()

    else:
        print("Unknown interpreter '{interpreter}'".format(
            interpreter=args.interpreter))
        sys.exit(1)

    if args.code is not None:
        interpreter.execute(args.code)

    if args.file is not None:
        if len(args.file) > 3 and args.file[-3:] == '.bf':
            try:
                with open(args.file) as f:
                    code = f.read()
                    interpreter.execute(code)

            except IOError:
                if args.interpreter == 'nice':
                    print("Could not find your file! "
                          "Please double check that the "
                          "path provided is accessible to me.")

                else:
                    print("Your code is broken. It failed.")

                sys.exit(1)

        else:
            if args.interpreter == 'nice':
                print("Invalid Brainfuck File!")

            else:
                print("Your code is broken. It failed.")

            sys.exit(1)

    if (args.code is not None or args.file is not None) and \
       not args.launch:
        sys.exit(1)

    while True:
        try:
            if stdout:
                code = raw_input("\n>>> ")

            else:
                code = raw_input(">>> ")

            # Get me the fuck out of here :)
            if code == 'GMTFOH':
                if args.interpreter == 'nice' or \
                   random() > 0.75:
                    sys.exit(0)

            elif code == 'PTRPLZ':
                if args.interpreter == 'nice' or \
                   random() > 0.75:
                    print(interpreter.ptr)

            elif match('^ARRPLZ\[\d*:\d*\]', code) or \
                 match('^ARRPLZ\[\d+]', code):
                if args.interpreter == 'nice' or \
                   random() > 0.75:
                    indices = code[6:]
                    print(eval("interpreter.array" + indices))

            else:
                stdout = interpreter.execute(code)

        except KeyboardInterrupt:
            stdout = False
