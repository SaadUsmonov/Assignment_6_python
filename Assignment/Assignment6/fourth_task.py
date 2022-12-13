def make_triple (number):
    arr = list()

    for item in range(number):
        i = input('Enter your number: ')
        i = int(i)
        arr.append(i)
    for item in range (0, len(arr)):
        if item + 2 == len(arr):
            summ = arr[item] + arr[item + 1] + arr[0]
            print(f'Triplet {item + 1}: {arr[item]} + {arr[item + 1]} + {arr[0]} = {summ}')
        elif item + 1 == len(arr):
            summ = arr[item] + arr[0] + arr[1]
            print(f'Triplet {item + 1}: {arr[item]} + {arr[0]} + {arr[1]} = {summ}')
        else:
            summ = arr[item] + arr[item + 1] + arr[item + 2]
            print(f'Triplet {item + 1}: {arr[item]} + {arr[item + 1]} + {arr[item + 2]} = {summ}')