#
# doubly.py
#     A simple program to solve the crossword.
#
# Author: Mike Smith
#
# Modification History:
#   M.R. Smith - 03-01-2026 - Initial version.
#                06-01-2026 - Add new constraints on cols 1 & 10.
#
import time

# Variables and defaults.
filled_sqr = '@'
vacant_sqr = '_'
ocount = 0
stop_row = 11
grid = ()
col_max = [1, 7, 1, 7, 1, 6, 6, 1, 7, 1, 7, 1]
col_cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
row_min = [3, 3, 4, 3, 4, 6, 6, 4, 3, 4, 3, 3]
N = 12
rows, cols = N, N
grid = [[vacant_sqr for _ in range(rows)] for _ in range(cols)]

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

def check_valid_cols(row):
    valid = True

    # Add cols 1 & 10 conditions.

    # Following should be filled (X).
    if row in [0, 2, 9, 11]:
        if grid[row][1]==vacant_sqr or grid[row][10]==vacant_sqr:
            valid = False

    if row in [3, 5, 7]:
        if grid[row][1]==vacant_sqr:
            valid = False

    if row in [4, 6, 8]:
        if grid[row][10]==vacant_sqr:
            valid = False

    # Following should be clear (_).
    if row in [1, 4, 6, 8, 10]:
        if grid[row][1]==filled_sqr:
            valid = False

    if row in [1, 3, 5, 7, 10]:
        if grid[row][10]==filled_sqr:
            valid = False

    return valid

def check_valid_rows(row):
    valid = True

    # Check minimum row totals
    for r in range(0, row+1):
        row_total = 0
        for c in range(0, N):
            if grid[r][c]==filled_sqr:
                row_total += 1
        if row_total < row_min[r]:
            valid = False

    return valid

def calc_perms(row, a, b ,c, d):
    if d > 0:
        a_end = 8-a-b-c-d
        b_end = 10-b-c-d
        c_end = 11-c-d
        d_end = 12-d
    elif c > 0:
        a_end = 9-a-b-c
        b_end = 11-b-c
        c_end = 12-c
    elif b > 0:
        a_end = 10-a-b
        b_end = 12-b
    if a > 0:
        a_end = 12-a

    for i in range(0, a_end+1):
        if set_grid_block(row, i, a):
            if row == 1 and check_valid_cols(row):
                calc_perms(row+1, 1, 1, 1, 1)
            if row == 5 and check_valid_cols(row):
                calc_perms(row+1, 6, 0, 0, 0)
            if row == 6 and check_valid_cols(row):
                calc_perms(row+1, 2, 1, 1, 0)

            if b > 0:
                for j in range(i+a+1, b_end+1):
                    # print(f'j {j} c {b} b_end {b_end}')
                    if set_grid_block(row, j, b):
                        if row == 1 and check_valid_cols(row):
                            calc_perms(row+1, 1, 1, 1, 1)
                        if row == 3 and check_valid_cols(row):
                            calc_perms(row+1, 1, 1, 2, 0)
                        if row == 8 and check_valid_cols(row):
                            calc_perms(row+1, 1, 1, 1, 1)
                        if row == 10 and check_valid_cols(row):
                            calc_perms(row+1, 1, 1, 1, 0)

                        if c > 0:
                            for k in range(j+b+1, c_end+1):
                                if set_grid_block(row, k, c):
                                    if row == 0 and check_valid_cols(row):
                                        calc_perms(row+1, 1, 2, 0, 0)
                                    if row == 4 and check_valid_cols(row):
                                        calc_perms(row+1, 6, 0, 0, 0)
                                    if row == 7 and check_valid_cols(row):
                                        calc_perms(row+1, 2, 1, 0, 0)

                                    if d > 0:
                                        for l in range(k+c+1, d_end+1):
                                            if set_grid_block(row, l, d):
                                                if row == 2 and check_valid_cols(row):
                                                    calc_perms(row+1, 1, 2, 0, 0)
                                                if row == 9 and check_valid_cols(row):
                                                    calc_perms(row+1, 2, 1, 0, 0)
                                            unset_grid_block(row, l, d)
                                    if row == stop_row and check_valid_cols(row) and check_valid_rows(row):
                                        show_grid(row)
                                unset_grid_block(row, k, c)
                    unset_grid_block(row, j, b)
        unset_grid_block(row, i, a)


start_time = time.perf_counter()
#
# Test a function that will output all the permutations of a row, for a given indicator.
#
calc_perms(0, 1, 1, 1, 0)

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")
