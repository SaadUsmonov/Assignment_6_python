def arr_creator():
    arr = list()
    counter = 0
    bol = False
    while counter <= 200:
        counter += 1
        a = input('Enter the positive number: ')
        a = int(a)
        if a < 0:
            break
        else:
            for item in arr:
                if item == a:
                    bol = True
                else:
                    continue
            if not bol:
                arr.append(a)
                bol = False
            else:
                bol = False
    for item in arr:
        print(item, end=" ")
