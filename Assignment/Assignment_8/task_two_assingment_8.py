def prime_numbers(int1):
    numarray = list({2})
    if int1 == 1:
        print(f'Input m: {int1}')
        print(f'The prime numbers <= {int1} are: 0')
        return
    if int1 == 2:
        print(f'Input m: {int1}')
        print(f'The prime numbers <= {int1} are: 2')
        return
    count = 1
    for i in range(3, int(int1)):
        if i / 2 == 0:
            continue
        number: int = int(i / 2) + 1
        for item in range(1, number):
            if i % item == 0:
                count += 1
        if count <= 2:
            numarray.append(i)
        count = 1
    print(f'The prime numbers <= {int1} are: ', end="")
    for item in numarray:
        print(item, end=" ")
    return
