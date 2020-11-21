from include.heart import Crack_Hash
import optparse,string,sys

raw_wordlist = string.ascii_lowercase

parser = optparse.OptionParser()
parser.add_option('-c','--code',dest='hash_code',metavar='your hash',type=str,action='store')
parser.add_option('--upper-case',dest='uppercase',default=False,const=string.ascii_uppercase,action='store_const',help='add wordlist with uppercase letter')
parser.add_option('--number',dest='number',default=False,action='store_const',const='0123456789',help='add wordlist with number')
parser.add_option('--max-range',dest='max_range',default=3,action='store',type=int,help='max wordlist to generate')
parser.add_option('--type-hash',dest='tipe_hash',action='store',help='type hash, supported (md5,sha512,sha1,sha256)')
parser.add_option('--symbols',dest='symbols',action='store_const',default=False,const='@#$%^&*()_+-=!|}{P[]~',metavar='add symbols like ()#&( .. etc to your wodlist')

(option,args) = parser.parse_args()

if option.uppercase:
    raw_wordlist += option.uppercase 
elif option.number:
    raw_wordlist += option.number
elif not option.tipe_hash or not option.hash_code:
    exit('Type hash/hash code is required, enter an option --help')

#print(option) # ?

if Crack_Hash(**vars(option),raw_wordlist=raw_wordlist).run_bitch():
    exit()
