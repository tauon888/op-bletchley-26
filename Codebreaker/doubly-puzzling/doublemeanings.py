#
# doublemeanings.py
#     A simple program to solve the double meaning clues.
#
# Author: Mike Smith
#
# Modification History:
#   M.R. Smith - 10-01-2026 - Initial version.
#
import time

# Variables and defaults.
clues = {
    1:'Boast (4)',
    2:'Close (e.g. with wax) (4)',
    3:'Complain (4)',
    4:'Lower the head (4)',
    5:'Endure (4)',
    6:'Stretch (e.g. the neck) (5)',
    7:'Struggle (e.g. in water) (8)',
    8:'Travel on ice (5)',
    9:'Chatter (3)'
}
sols = {
    1:['BRAG', 'CROW'],
    2:['SEAL'],
    3:['MOAN', 'CARP', 'NAGS'],
    4:['BEND', 'NODS', 'DUCK', 'BEND', 'PRAY', 'DIPS', 'BOWS'],
    5:['BEAR','LAST'],
    6:['CRANE', 'REACH'],
    7:['FLOUNDER'],
    8:['SKATE', 'SKIES', 'GLIDE', 'SLIDE'],
    9:['YAK', 'GAB', 'GAS']
}
'''
sols = {
    1:['BRAG'],
    2:['SEAL'],
    3:['MOAN'],
    4:['BEND', 'NODS'],
    5:['LAST'],
    6:['CRANE'],
    7:['FLOUNDER'],
    8:['SKATE'],
    9:['GAS', 'GAB']
}
'''


start_time = time.perf_counter()
#
# Test a function that will output all the permutations of a row, for a given indicator.
#
count = 0
list = []
soln = []
for s1 in sols[1]:
    list.append(s1)
    for s2 in sols[2]:
        list.append(s2)
        for s3 in sols[3]:
            list.append(s3)
            for s4 in sols[4]:
                list.append(s4)
                for s5 in sols[5]:
                    list.append(s5)
                    for s6 in sols[6]:
                        list.append(s6)
                        for s7 in sols[7]:
                            list.append(s7)
                            for s8 in sols[8]:
                                list.append(s8)
                                for s9 in sols[9]:
                                    list.append(s9)
                                    count += 1
                                    #print(f'{count} {s1} {s2} {s3} {s4} {s5} {s6} {s7} {s8} {s9} ')
                                    sorted_list = sorted(list)
                                    print(f'{count} {sorted_list} ')

                                    # Assume 3 colums down then across.
                                    ans = sorted_list[4][2:3] + sorted_list[6][0:1]
                                    ans += sorted_list[7][0:1] + sorted_list[3][0:1]
                                    ans += sorted_list[2][1:2] + sorted_list[0][1:2]
                                    ans += sorted_list[7][1:2] + sorted_list[5][0:1]
                                    print(f'D       {sorted_list[0]:8} {sorted_list[3]:8} {sorted_list[6]:8} ')
                                    print(f'        {sorted_list[1]:8} {sorted_list[4]:8} {sorted_list[7]:8} ')
                                    print(f'        {sorted_list[2]:8} {sorted_list[5]:8} {sorted_list[8]:8} ')
                                    print(f'D {count} {ans} ')
                                    if ans not in soln:
                                        soln.append(ans)

                                    # Assume 3 rows across then down.
                                    ans = sorted_list[4][2:3] + sorted_list[2][0:1]
                                    ans += sorted_list[5][0:1] + sorted_list[1][0:1]
                                    ans += sorted_list[6][1:2] + sorted_list[0][1:2]
                                    ans += sorted_list[5][1:2] + sorted_list[7][0:1]
                                    print(f'A       {sorted_list[0]:8} {sorted_list[1]:8} {sorted_list[2]:8} ')
                                    print(f'        {sorted_list[3]:8} {sorted_list[4]:8} {sorted_list[5]:8} ')
                                    print(f'        {sorted_list[6]:8} {sorted_list[7]:8} {sorted_list[8]:8} ')
                                    print(f'A {count} {ans} ')
                                    if ans not in soln:
                                        soln.append(ans)

                                    list.remove(s9)
                                list.remove(s8)
                            list.remove(s7)
                        list.remove(s6)
                    list.remove(s5)
                list.remove(s4)
            list.remove(s3)
        list.remove(s2)
    list.remove(s1)

for s in soln:
    print(s, s[::-1])

print()
for s in soln:
    print(s, end=" ")
print()

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.4f} seconds")
