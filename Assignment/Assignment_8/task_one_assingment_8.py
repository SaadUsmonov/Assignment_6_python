def gdc():
    int1 = int(input('Enter the numerator: '))
    int2 = int(input('Enter the denominator: '))
    temp1 = int1
    temp2 = int2
    while temp2 != 0:
        temp = temp2
        temp2 = temp1 % temp2
        temp1 = temp

    hcf = temp1

    print(f'Result: {int1}/{int2} = {int(int1 / hcf)}/{int(int2 / hcf)}')
    return
