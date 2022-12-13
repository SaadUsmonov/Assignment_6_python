# Write a Python program for:
#     • Loading an array v of DIM (DIM is a constant) integer numbers.
# • Copying all its positive elements into an array named vp and all its negative ones into
# another array named vn.
# • Displaying the contents of vp and vn (only the values copied from v).
# Example: let DIM = 10 and assume that the following array has been introduced:
# v = [18 11 -4 5 0 0 -2 3 25 0]
# Then, the following two arrays must be generated and displayed:
# vp = [18 11 5 3 25]
# vn = [-4 -2]

import array as array


def positive_and_negative(list):
    v = array.array('i', list)
    vp = array.array('i', {})
    vn = array.array('i', {})
    for item in v:
        if item > 0:
            vp.append(item)
        elif item < 0:
            vn.append(item)
    print(f'Positive Numbers: {vp}\nNegative Numbers: {vn}')

