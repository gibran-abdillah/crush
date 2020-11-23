# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : wordlist.py
# Last Modified : 11/23/20, 02:01 PM
# Copyright © 2020 Relarizky x Gibran


import os
from argparse import ArgumentParser as ArgParseClass
from crushasher.general.interface import default_banner


class ArgumentParser(ArgParseClass):

    @default_banner
    def print_help(self):
        super(ArgumentParser, self).print_help()

    def error(self, message):
        self.print_help()
        os._exit(1)


parser = ArgumentParser(
    description="Simple Tool For Hash Cracking",
    epilog="Happy Cracking:)",
    usage="crush.py -s <hash> [-d | -b] [-w <file> | -l <length number>]",
    prog="crush.py")
groups = parser.add_mutually_exclusive_group()

parser.add_argument("-s", "--string",
                    help="hash string you'd like to crack",
                    required=True)
groups.add_argument("-b", "--brute-attack",
                    help="perform brute-force attack", action="store_true")
groups.add_argument("-d", "--dict-attack",
                    help="perform dictionary attack", action="store_true")
parser.add_argument("-l", "--length",
                    help="max length of string for brute-forcing (default=3)",
                    default=3, type=int)
parser.add_argument("-w", "--wordlist",
                    help="wordlist file for dictionary attack")

argument = parser.parse_args()
