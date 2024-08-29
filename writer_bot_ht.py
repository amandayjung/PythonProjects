'''
File: writer_bot_ht.py
Author: Amanda Jung
Course: CSC 120, Spring 2024
Purpose: TBR
'''

import random
import sys
SEED = 8
NONWORD = "@"

class Hashtable:
    def __init__(self, size):
        self._pairs = [None] * size
        self._size = size

    def _hash(self, key):
        p = 0
        for c in key:
            p = 31 * p + ord(c)
        return p % self._size

    def put(self, key, value):
        index = self._hash(key)
        while self._pairs[index] is not None:
            index = (index - 1) % self._size
        self._pairs[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        while self._pairs[index] is not None:
            k, v = self._pairs[index]
            if k == key:
                return v
            index = (index - 1) % self._size
        return None

    def __contains__(self, key):
        return self.get(key) is not None

    def __str__(self):
        return str(self._pairs)

def build_chain(sfile, n, hashtable):
        file = open(sfile, 'r')
        words = file.read().split()
        chain = {}
        prefix = [NONWORD] * n
        for word in words:
            key = ' '.join(prefix)
            if key in hashtable:
                hashtable.get(key).append(word)
            else:
                hashtable.put(key, [word])
            prefix.pop(0)
            prefix.append(word)
        key = ' '.join(prefix)
        if key in hashtable:
            hashtable.get(key).append(NONWORD)
        else:
            hashtable.put(key, [NONWORD])

def generate_text(hashtable, n, num_words):
    random.seed(SEED)
    prefix = [NONWORD] * n
    text = []
    for _ in range(num_words):
        key = ' '.join(prefix)
        suffixes = hashtable.get(key)
        if suffixes:
            suffix = random.choice(suffixes)
            if suffix != NONWORD:
                text.append(suffix)
                prefix.pop(0)
                prefix.append(suffix)
            else:
                break  
        else:
            break 
    return text

def print_output(text):
    for i in range(0, len(text), 10):
        print(' '.join(text[i:i+10]))

def main():
    sfile = input()
    M = int(input())
    n = int(input())
    num_words = int(input())
    if n < 1:
        print("ERROR: specified prefix size is less than one")
        sys.exit(0)
    if num_words < 1:
        print("ERROR: specified size of the generated text is less than one")
        sys.exit(0)
    hashtable = Hashtable(M)
    build_chain(sfile, n, hashtable)
    text = generate_text(hashtable, n, num_words)
    print_output(text)

main()
