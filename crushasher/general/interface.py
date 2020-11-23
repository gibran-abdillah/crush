# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : wordlist.py
# Last Modified : 11/23/20, 01:49 AM
# Copyright © 2020 Relarizky x Gibran


from functools import wraps


def default_banner(function):
    @wraps(function)
    def banner(*args, **kwargs):
        print("  _____                _")
        print(" / ____|              | |")
        print("| |     _ __ _   _ ___| |__")
        print("| |    | '__| | | / __| '_ \\")
        print("| |____| |  | |_| \\__ \\ | | |")
        print(" \\_____|_|   \\__,_|___/_| |_|")
        print("            [Crack Your Hash]\n")
        return function(*args, **kwargs)
    return banner
