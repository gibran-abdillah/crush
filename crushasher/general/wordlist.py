# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : wordlist.py
# Last Modified : 11/23/20, 08:36 AM
# Copyright © 2020 Relarizky x Gibran


import os


def is_file_exist(file_name: str) -> bool:
    """ check existence of the wordlist file """

    return os.path.isfile(file_name)


def read_word_list(file_name: str, divide_into: int = 5) -> list:
    """ read wordlist and remove its duplicated/empty elements """

    # flake8 says do not use lambda :p
    def remove_whitespace(element):
        return element.strip()

    with open(file_name, "r", encoding="latin1") as word_list:
        word_list = map(remove_whitespace, word_list.readlines())
        return word_list
