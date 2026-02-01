#
# final.py
#     A simple program to solve the elements.
#
# Author: Mike Smith
#
# Modification History:
#   M.R. Smith - 19-01-2026 - Initial version.
#
import time

# Variables and defaults.
alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def show_grid(row):
    global ocount
    ocount += 1
    for i in range(stop_row+1):
        print('|', end="")
        for j in range(N):
            print(f'{grid[i][j]}|', end="")
        if i == 0:
            print(f' ({ocount:,})')
        else:
            print()
    print()

def set_grid(row, col):
    grid[row][col]=filled_sq

def unset_grid_block(row, col, length):
    for i in range(col, col+length):
        grid[row][i]=vacant_sqr
        col_cnt[i] -= 1

def set_grid_block(row, col, length):
    valid = True

    for i in range(col, col+length):
        grid[row][i]=filled_sqr
        col_cnt[i] += 1
        if col_cnt[i] > col_max[i]:
            valid = False

    return valid


start_time = time.perf_counter()
#
# Test a function that will output all the permutations of a row, for a given indicator.
#
'''
table = [81, 20, 71, 86, 48, 54, 40, 32, 46]
for i in table:
    print(f'{i} ', end="")
print()
for i in table:
    i += 13
    k = i % 27
    if i >= 27:
        k += 1
    print(f'{alphabet[k]} ', end="")
print()
'''
#str = 'wnlbpvhzn'
str = 'tlcaluracdxezrgepa'
# ASCII range 97-122.
for i in range(27):
    new_str = ''
    for s in str:
        c = ord(s)
        new_c = c + i
        if new_c > 122:
            new_c = new_c - 26
        new_s = chr(new_c)
        # print(f'{s} {new_s}')
        new_str += new_s
    #print(i, new_str)
    print(new_str, end=" ")
print()

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")
