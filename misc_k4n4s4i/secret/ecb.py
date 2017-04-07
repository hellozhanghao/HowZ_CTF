#!/usr/bin/env python3

# Done by Alice

from solver import LinearPresent
from misc_k4n4s4i/secret/present import *
import argparse

i2b = lambda i: i.to_bytes(8, byteorder='little')
b2i = lambda b: int.from_bytes(b, byteorder='little')

def iterate_bytes(inp):
    for i in range(len(inp)//8):
        byte = inp[i*8:i*8+8]
        yield byte

def encrypt(inp, key):
    enc = lambda b: i2b(present(b2i(b), key))
    return b''.join(b for b in map(enc, iterate_bytes(inp)))

def decrypt(inp, key):
    dec = lambda b: i2b(present_inv(b2i(b), key))
    # linear_algebra_decryptor = LinearPresent('./pair')
    # dec = lambda b: i2b(linear_algebra_decryptor.decrypt(b2i(b)))
    return b''.join(b for b in map(dec, iterate_bytes(inp)))

def ecb(infile,outfile,key,mode):
    run = {'e': encrypt, 'd': decrypt}

    with open(key, 'rb') as f:
        key = b2i(f.read())
    
    # run encrypt() or decrypt() based on the mode entered by user
    with open(outfile, 'wb') as out:
        with open(infile, 'rb') as inp:
            inp = inp.read()
        output = run[mode](inp, key)
        out.write(output)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode', 
                        choices=('e', 'd'))

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    key=args.keyfile
    mode=args.mode

    ecb(infile,outfile,key,mode)

