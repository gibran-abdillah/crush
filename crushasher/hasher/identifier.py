# Author : Relarizky & Gibran
# Github : @relarizky & @gibran-abdillah
# File   : identifier.py
# Last Modified : 11/22/20, 13:58 PM
# Copyright © 2020 Relarizky x Gibran


class HashLengthChecker:
    """ identify hash type by checking its length """

    @staticmethod
    def is_md5(string: str) -> bool:
        return len(string) == 32

    @staticmethod
    def is_sha1(string: str) -> bool:
        return len(string) == 40

    @staticmethod
    def is_sha256(string: str) -> bool:
        return len(string) == 64

    @staticmethod
    def is_sha512(string: str) -> bool:
        return len(string) == 128


class HashIdentifier(HashLengthChecker):
    """ main class/client interface of hash identifier """

    def __init__(self, string: str):
        self.__identify(string)

    def __str__(self):
        return self.hash

    # Private Method
    # Should not be accessed outside this class
    # And will not be inherited to the sub class
    def __identify(self, string: str):
        if self.is_md5(string):
            self.hash = "md5"
        elif self.is_sha1(string):
            self.hash = "sha1"
        elif self.is_sha256(string):
            self.hash = "sha256"
        elif self.is_sha512(string):
            self.hash = "sha512"
        else:
            self.hash = "unknown"
