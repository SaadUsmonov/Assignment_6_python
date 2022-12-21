def n_exp_n(int1):
    if int1 == 1:
        print('Maximum x = 1')
        return
    for item in range(1, int(int1 / 2)):
        sum_pow = 1
        maximum = item - 1
        for i in range(1, item + 1):
            sum_pow *= item
        if sum_pow > int1:
            print(f'Maximum x = {maximum}')
            return
