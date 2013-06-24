#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import sys, base64, hashlib

def revbits(x):
    return int(bin(x)[2:].zfill(8)[::-1], 2)

def compute_keypart(data, pos):
    dict_b64 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=\n"
    keys = range(256)
    
    j = pos
    while len(keys) > 1 and j < len(data):
        r_data = sum(1<<(7-i) for i in range(8) if ord(data[j])>>i&1)
        for k in keys:
            if chr(k ^ r_data) not in dict_b64:
                keys.remove(k)
        j += 16
    if len(keys) != 1:
        print "Warning : several candidates for position %d - %s" % (pos, keys)
    return "%0.2x" % keys[0]

def decrypt(data, key):
    output = open("data.clear", "wb")
    k = key.decode('hex')
    s = ''
    for j in range(len(data)):
        atad = sum(1<<(7-i) for i in range(8) if ord(data[j])>>i&1)
        s += chr(ord(k[j%16]) ^ atad)
    print "md5(s): ", hashlib.md5(s).hexdigest()
    output.write(base64.b64decode(s))

    print "Decyrption done in file data.clear"
    
data = open("D:\\sstic2013\\archive\\data", "rb").read()
key = ''.join([compute_keypart(data, i) for i in range(16)])

print "Key found ! - ", key
print "Decrypting data file..."
decrypt(data, key)
