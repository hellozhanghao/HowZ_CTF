import hashlib
import time



alphabet = 'abcdefghijklmnopqrstuvwxyz'

def append(digit, word):


    if digit == 0:
        key = hashlib.md5(word.encode('ascii')).hexdigest()
        # print(word,key)



    else:
        for i in alphabet:
            append(digit - 1, word + i)





start_time = time.time()

append(5,'')

print("Time taken: ", time.time()-start_time,"s")