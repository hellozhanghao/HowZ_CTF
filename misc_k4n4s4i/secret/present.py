#!/usr/bin/env python3

# Present skeleton file for 50.020 Security
# Oka, SUTD, 2014

# Done by Alice

#constants
fullround=31

#S-Box Layer
# sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]

# this simple modification should make my code run 100x faster, hehehe
sbox=[i for i in range(16)]

#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]
pmt_inv = [pmt.index(i) for i in range(len(pmt))]

# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def set_bit(n, val, pos):
    return n ^ ((-val ^ n) & (1 << pos))

def get_bit(n, pos):
    return (n >> pos) & 1

def genRoundKeys(key):
    # sbox(18,17,16,15)
    # xor(38,37,36,35,34)
    keys = [key]
    for i in range(1, 32):
        key = ror(key, 15, 80)
        key = (key & 0xfffffffffffffffffff0) + sbox[key & 0xf]
        key = ror(key, 19, 80)
        key ^= i
        key = rol(key, 15, 80)
        keys.append(key)
    return keys

def addRoundKey(state,Ki):
    return state ^ Ki

def sBoxLayer(state, inv=False):
    sbox_func = lambda s, inv: sbox.index(state & 0xf) if inv \
                                else sbox[state & 0xf]
    new_state = 0
    for i in range(16):
        new_state += sbox_func(state, inv)
        new_state = ror(new_state, 4, 64)
        state >>= 4
    return new_state

def pLayer(state, inv=False):
    pmt_map = pmt_inv if inv else pmt
    new_state = 0
    for i, Pi in enumerate(pmt_map):
        new_state = set_bit(new_state, get_bit(state, i), Pi)
    return new_state

def present_rounds(plain, key, rounds, inv=False):
    state = plain

    keys = genRoundKeys(key)
    keys = keys[::-1] if inv else keys

    update = lambda s, inv: sBoxLayer(pLayer(s, inv), inv) if inv \
                             else pLayer(sBoxLayer(s))

    for i in range(len(keys)):
        state = addRoundKey(state, keys[i] >> 16)
        if i == 31:
            break
        state = update(state, inv)

    return state

def present(plain, key):
    return present_rounds(plain, key, fullround)

def present_inv(plain, key):
    return present_rounds(plain, key, fullround, inv=True)



if __name__=="__main__":

    plain1 = 0x0
    key1 = 0x0
    cipher1 = present(plain1,key1)
    plain11 = present_inv(cipher1,key1)
    print(format(cipher1,'x'))

    plain1 = 0x2
    key1 = 0x2
    cipher1 = present(plain1, key1)
    plain11 = present_inv(cipher1, key1)
    print(format(cipher1, 'x'))
