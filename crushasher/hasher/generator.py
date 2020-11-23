# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : generator.py
# Last Modified : 11/22/20, 14:09 PM
# Copyright © 2020 Relarizky x Gibran


import hashlib


class HashStringGenerator:
    """ create/generate hash (md5,sha1,sha256,sha512) """

    @staticmethod
    def md5(string: str) -> str:
        return hashlib.md5(
            string.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def sha1(string: str) -> str:
        return hashlib.sha1(
            string.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def sha256(string: str) -> str:
        return hashlib.sha256(
            string.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def sha512(string: str) -> str:
        return hashlib.sha512(
            string.encode("utf-8")
        ).hexdigest()


class HashGenerator(HashStringGenerator):
    """ main class/client interface of hash generator """

    def __init__(self, type: str, plain_text: str):
        self.__generate(type, plain_text)

    def __str__(self):
        return self.hash_string

    # Private Method
    # Should not be accessed outside this class
    # And will not be inherited to the sub class
    def __generate(self, type: str, string: str):
        if type == "md5":
            self.hash_string = self.md5(string)
        elif type == "sha1":
            self.hash_string = self.sha1(string)
        elif type == "sha256":
            self.hash_string = self.sha256(string)
        elif type == "sha512":
            self.hash_string = self.sha512(string)
