def square_maker():
    n = int(input('Input the number of elements  : '))
    m = int(input('Input the size of each element: '))

    for item in range(m + 2):
        for i in range(n):
            if item == 0 or item == m + 1:
                if i == 0 and n != 0:
                    print('+--+', end="")
                    continue
                print('--+', end="")
                continue
            print('|', end="  ")
        if item != 0 and item != m + 1:
            print('|', end="  ")
        print()


