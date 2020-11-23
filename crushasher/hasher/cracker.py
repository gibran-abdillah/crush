# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : cracker.py
# Last Modified : 11/22/20, 16:45 PM
# Copyright © 2020 Relarizky x Gibran


import time
import itertools
from crushasher.hasher.generator import HashGenerator
from crushasher.general.wordlist import read_word_list


class SuccessfullyCracked(Exception):
    """ raised when the hash successfully cracked for exitting the program """
    pass


class DictionaryAttack:

    # Protected Attribute
    # this attribute implies the start time of the program
    _start_time = time.time()

    def __init__(self, type, hash, word_list):
        self.type = type
        self.hash = hash
        self.word_list = word_list

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type is not None:
            if type is KeyboardInterrupt:
                print("[-] You exited this program!")
            elif type is SuccessfullyCracked:
                print("[+] Done in %.2f seconds" % (time.time()-self._start_time))
                print("[+] The hash has successfully cracked!")
            else:
                print("[-] Program exited due to some error, {}".format(type))
        else:
            print("[-] Sorry, we can't find the result:(")

        return True

    # Protected Method
    # Should not be accessed outside the class
    # inheritable to the sub class
    def _compare(self, string: str) -> bool:
        hash_string = HashGenerator(self.type, string)
        if self.hash == str(hash_string):
            return "[+] Your result is : {}".format(string)

    def crack(self):
        word_list = read_word_list(self.word_list)
        for word in word_list:
            dict_attack = self._compare(word)
            if dict_attack is not None:
                print(dict_attack)
                raise SuccessfullyCracked


class BruteForce(DictionaryAttack):

    # Private Attribute
    # This attribute implies the number of created string
    __string_created = 0

    # Private Attribute
    # This attribute implies the minimum of string length
    __min_length = 0

    def __init__(self, type, hash, length):
        self.type = type
        self.hash = hash
        self.length = 3 if length < 3 else length
        DictionaryAttack.__init__(self, type, hash, None)

    # override method from the parent class
    def crack(self):
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        for repeat in range(self.__min_length, self.length+1):
            print("[+] Brute Forcing with {} length string".format(str(repeat)))
            for word in itertools.product(characters, repeat=repeat):
                word = "".join(str(char) for char in word).strip()
                brute = self._compare(word)
                if brute is not None:
                    print(brute)
                    print("[+] {} strings created".format(str(self.__string_created)))
                    raise SuccessfullyCracked
                self.__string_created += 1
