# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : wordlist.py
# Last Modified : 11/23/20, 14:45 PM
# Copyright © 2020 Relarizky x Gibran


import os
from crushasher.hasher.cracker import DictionaryAttack, BruteForce
from crushasher.hasher.identifier import HashIdentifier
from crushasher.general.interface import default_banner
from crushasher.general.wordlist import is_file_exist
from crushasher.general.argument import argument


@default_banner
def main(hash, word_list=None, length=None, **technique):
    type = HashIdentifier(hash)

    if str(type) == "unknown":
        print("[-] We can't identify your hash type.")
        os._exit(1)

    print("[+] Your hash identified as : {}".format(type))
    if "dict_attack" in technique and technique["dict_attack"] is True:
        with DictionaryAttack(str(type), hash, word_list) as dictionary_attack:
            dictionary_attack.crack()
    elif "brute_force" in technique and technique["brute_force"] is True:
        with BruteForce(str(type), hash, length) as brute_force:
            brute_force.crack()


if __name__ == "__main__":
    hash_string = argument.string
    word_list_file, length = argument.wordlist, argument.length
    brute_force, dict_attack = argument.brute_attack, argument.dict_attack

    if brute_force is False and dict_attack is False:
        print("[!] Please specify the technique!")
        os._exit(1)

    if brute_force is True:
        main(hash_string, length=length, brute_force=True)

    if dict_attack is True:
        if word_list_file is None:
            print("[!] You need to specify wordlist to perform this attack!")
            os._exit(1)
        if not is_file_exist(word_list_file):
            print("[-] File {} does not exist!".format(word_list_file))
            os._exit(1)

        main(hash_string, word_list=word_list_file, dict_attack=True)
