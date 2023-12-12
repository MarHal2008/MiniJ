# sha224
# sha256
# md5
import hashlib
# x = input()
# sha224 = hashlib.sha224(x.encode())
# print(f"sha224 for x = ,{sha224.hexdigest()}")
import sys


def hashCracking(format):
    with open(wordlist_pathway, "p") as p:
        for i in p:
            print(i.strip())
    if format == "md5":
        hashlib.md5(p.decode)
    elif format == "sha224":
        hashlib.sha224(p.decode)
    elif format == "sha256":
        hashlib.sha256(p.decode)


if len(sys.argv) == 4:
    format = sys.argv[1]
    wordlist_pathway = sys.argv[2]
    hash = sys.argv[3]
    hashCracking(format, wordlist_pathway, hash)
else:
    print("I need more arguments!")
