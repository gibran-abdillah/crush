import hashlib
import itertools
import sys,time

class Crack_Hash:
    def __init__(self,**kwargs):
        self.hash_code = kwargs.get('hash_code')
        self.raw_wordlist = kwargs.get('raw_wordlist')
        self.tipe_hash = kwargs.get('tipe_hash')
        self.max_range = kwargs.get('max_range')
        self.min_range = 3
        if self.max_range <= self.min_range:
            self.max_range = self.min_range + self.max_range
    
    def run_bitch(self):
        try:

            dict_to_execute = {'md5':self.encode_md5,'sha512':self.encode_sha512,'sha384':self.encode_sha384,'sha256':self.encode_sha256,'sha1':self.encode_sha1}
            solved = []
            start_time = time.time()
            
            for _ in range(self.min_range,self.max_range+1):
                word_generated = []
                for wordlists in itertools.product(self.raw_wordlist,repeat=_):
                    self.my_word = ''.join(str(__) for __ in wordlists)
                    word_generated.append(self.my_word)
                    if dict_to_execute[self.tipe_hash]() == self.hash_code:
                        solved.append(self.my_word)
                    sys.stdout.write('\r[+] Bruteforcing with length {}'.format(len(self.my_word)))

                if len(solved) != 0:
                    print('\n[+] Cracked  {}'.format(solved[0]))
                    all_time = str(time.time() - start_time).split('.')[0]
                    print('[+] in {} seconds'.format(all_time))
                    print('[+] wordlist loaded {}'.format(len(word_generated)))
                    return True 
                    
        except KeyError:
            exit('Your tipe hash is not supported :(')

    def encode_md5(self):
        return hashlib.md5(self.my_word.encode('utf-8')).hexdigest()

    def encode_sha512(self):
        return hashlib.sha512(self.my_word.encode('utf-8')).hexdigest()
    
    def encode_sha256(self):
        return hashlib.sha256(self.my_word.encode('utf-8')).hexdigest()
    
    def encode_sha384(self):
        return hashlib.sha384(self.my_word.encode('utf-8')).hexdigest()
    
    def encode_sha1(self):
        return hashlib.sha1(self.my_word.encode('utf-8')).hexdigest()
    

