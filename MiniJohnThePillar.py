# sha224
# sha256
# md5
import hashlib
import sys


def hashed_sha224(word):
    hash_value = hashlib.sha224(f"{word}".encode('utf-8'))
    hashed = hash_value.hexdigest()
    return hashed


def hashed_sha256(word):
    hash_value = hashlib.sha256(f"{word}".encode('utf-8'))
    hashed = hash_value.hexdigest()
    return hashed


def hashed_md5(word):
    hash_value = hashlib.md5(f"{word}".encode('utf-8'))
    hashed = hash_value.hexdigest()
    return hashed


wordhash = sys.argv[1]
formant = sys.argv[2]
wordlist_pathway = sys.argv[3]


def hashCracking(formant, wordlist_pathway, wordhash):
    with open(wordlist_pathway, "r") as file:
        for line in file:
            for word in line.split():
                if format == "md5":
                    if hashed_md5(word) == wordhash:
                        return word
                elif format == "sha224":
                    if hashed_sha224(word) == wordhash:
                        return word
                elif format == "sha256":
                    if hashed_sha256(word) == wordhash:
                        return word


solvedWord = hashCracking(wordhash, formant, wordlist_pathway)
if solvedWord:
    print(f"Cracked hash: {solvedWord}")
else:
    print("I need more arguments!")
