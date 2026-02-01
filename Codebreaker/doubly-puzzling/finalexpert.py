#
# final.py
#     A program to adjust the words to get the letter pairs.
#
# Author: Mike Smith
#
# Modification History:
#   M.R. Smith - 30-01-2026 - Initial version.
#
import time

# Variables and defaults.
alpha2num = {
    'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8,
    'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15,
    'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22,
    'W':23, 'X':24, 'Y':25, 'Z':26
}
num2alpha = {
    1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H',
    9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O',
    16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V',
    23:'W', 24:'X', 25:'Y', 26:'Z'
}

testStr = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"




def shift_alpha(str, shift):
    i = 0
    ans = ''
    for c in str:
        n = alpha2num[c]
        offset = shift[i]
        i += 1
        m = num2alpha[n + offset]
        ans += m
    return ans


start_time = time.perf_counter()

tests = {
    'GROVEL':[-6,-14,-14,-3,-4,10],
    'CAVEAT':[-1,8,-18,4,4,-1],
    'STIMULUS':[-11,-15,0,-11,-12,-9,-9,-14],
    'BELIEF':[11,0,2,-5,9,-1],
    'TROPICAL':[-6,2,0,4,7,-2,15,-7],
    'CLACKING':[13,3,17,-2,7,6,4,18],
    'MANTRA':[7,15,7,-2,3,17]
}
for k,v in tests.items():
    print(k, shift_alpha(k, v))

print()

revs = {
    'ESETGAGG':[11,-14,-1,-15,12,19,-6,5],
    'SSTETO':[-15,-14,-14,4,-15,-11]
}
for k,v in revs.items():
    print(k, shift_alpha(k, v))



end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")
