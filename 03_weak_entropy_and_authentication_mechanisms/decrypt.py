#!/usr/bin/env python3

import random
import sys
import time
import datetime
from Crypto.Cipher import AES


def encrypt(input_file):
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
    nonce = data[:16]
    tag = data[16:32]
    cypher = data[32:]

    n_seconds = 24 * 60 * 60
    timestamp = int(datetime.datetime(2024, 2, 20).timestamp())
    for i in range(0,n_seconds):
        seed = timestamp - i
        random.seed(seed)
        key = random.randbytes(16)
        aes = AES.new(key, AES.MODE_GCM, nonce=nonce)
        try:
            plaintext = aes.decrypt_and_verify(cypher, tag)
            print(plaintext)
        except:
            pass


if __name__ == '__main__':
    encrypt(sys.argv[1])
