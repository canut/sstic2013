#!/opt/local/bin/python2.7
# -*- coding: utf-8 -*-


import base64, hashlib
from scapy.all import *
from Crypto.Cipher import AES

def create_key(ti, to, ttl):
    #time | tos | ttl
    key1 = ''.join([hex((ti[i] << 3) + (to[i] << 2) + ttl[i])[2] for i in range(len(ti))])
    key1 = '0' * (64 - len(key1)) + key1
    
    #time | ttl | tos
    key2 = ''.join([hex((ti[i] << 3) + (ttl[i] << 1) + to[i])[2] for i in range(len(ti))])
    key2 = '0' * (64 - len(key2)) + key2
    return [key1, key2]

def decrypt(ciph, key, mode):
    chainmode = {"CBC" : AES.MODE_CBC,
                 "ECB" : AES.MODE_ECB,
                 "CFB" : AES.MODE_CFB,
                 "CTR" : AES.MODE_CTR,
                 "OFB" : AES.MODE_OFB}
    
    IV = "76C128D46A6C4B15B43016904BE176AC"
    obj = AES.new(key.decode('hex'), chainmode[mode], IV.decode('hex'))
    clear = obj.decrypt(ciph)
    padding = ord(clear[-1])
    clear = clear[:-padding]
    if check_md5(clear):
        print "Decryption done with key %s in mode %s!!" % (key, mode)
        outfile = open("./sstic.tar.gz", 'w')
        outfile.write(clear)
        outfile.close()

def check_md5(s):
    return hashlib.md5(s).hexdigest() == "61c9392f617290642f9a12499de6b688"

def extract_bits(p):
    t = [int(round(p[i+1].time-p[i].time,0))-1 for i in range(5,69)]
    u = [(p[i][IP].tos-2)/2 for i in range(5,69)]
    return (t, u)

def extract_ttl(p, m):
    tab = dict(zip([10, 20, 30, 40], m))
    return [tab[p[i][IP].ttl] for i in range(5,69)]

p = rdpcap("./dump.bin")
time_bits, tos_bits = extract_bits(p)

keys = []
for b1 in [time_bits, [b^1 for b in time_bits]]:
    for b2 in [tos_bits, [b^1 for b in tos_bits]]:
        for b3 in [extract_ttl(p, m) for m in itertools.permutations([0, 1, 2, 3], 4)]:
            keys.extend(create_key(b1, b2, b3))

ciph = base64.b64decode(open("./sstic.tar.gz-chiffre", 'r').read())

print "Key candidates: %d" % len(keys)

for k in keys:
    if len(k) == 64:
        decrypt(ciph, k, "CBC")
        decrypt(ciph, k, "CFB")
        decrypt(ciph, k, "OFB")

        
