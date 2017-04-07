from present import *

pmt = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51,
       4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23, 39, 55,
       8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59,
       12, 28, 44, 60, 13, 29, 45, 61, 14, 30, 46, 62, 15, 31, 47, 63]

p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
     60, 61, 62, 63]

p_pmt = [0, 16, 32, 48, 1, 17, 33, 49, 2, 18, 34, 50, 3, 19, 35, 51, 4, 20, 36, 52, 5, 21, 37, 53, 6, 22, 38, 54, 7, 23,
         39, 55, 8, 24, 40, 56, 9, 25, 41, 57, 10, 26, 42, 58, 11, 27, 43, 59, 12, 28, 44, 60, 13, 29, 45, 61, 14, 30,
         46, 62, 15, 31, 47, 63]

p_pmt_1 = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49,
           53, 57, 61, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 3, 7, 11, 15, 19, 23, 27, 31, 35,
           39, 43, 47, 51, 55, 59, 63]

# print(p0)



def set_bit(n, val, pos):
    return n ^ ((-val ^ n) & (1 << pos))

def get_bit(n, pos):
    return (n >> pos) & 1


# for i in pmt


message = 16512490488185588596
cipher = 7969565605816525137

pmt_inv = [pmt.index(x) for x in range(0,64)]


print(pLayer(message)^cipher)

message2 = 7858514579842233755
cipher2= 12170563608508527832

print(pLayer(message2)^cipher2)

key = 18236570854242329511

f = open("not_a_diary.e",'rb')
b = f.read(8)
while b!=b'':
    cipher = int.from_bytes(b, byteorder='little')
    #print(cipher)
    plaintext = pLayer(cipher^key, inv=True)
    print(plaintext.to_bytes(8,byteorder='little'))


    b = f.read(8)

st= "Dear diary,\n\nThis is my first entry. I'm so happy about it! Today I caught a hering\nin runescape. I love herings!\n\n<3,\ncheshirecat\n\n\n\n\n\n"
print(st)