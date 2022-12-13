def find_sub_array(number):
    arr = list()
    list()
    for item in range (number):
        a = input('Enter the number: ')
        arr.append(int(a))

    for item in range(0, len(arr)):
        summa = arr[item]
        index = item
        for sub_item in range(item + 1, len(arr)):
            summa += arr[sub_item]
            if summa == 0:
                print(f'Sub-array starting from index {index}, length {sub_item + 1 - index}')
            else:
                continue
