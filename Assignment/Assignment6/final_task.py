def create_vertical_histogram():
    _r_9 = 0
    _r_10 = 0
    _r_20 = 0
    _r_30 = 0
    _r_40 = 0
    _r_50 = 0
    _r_60 = 0
    _r_70 = 0
    _r_80 = 0
    _r_90 = 0

    bool = True
    while bool:
        a = input('Enter your number: ')
        a = int(a)
        if a < 0 or a > 99:
            bool = False
        if a in range(0, 10):
            _r_9 += 1
        elif a in range(10, 20):
            _r_10 += 1
        elif a in range(20, 30):
            _r_20 += 1
        elif a in range(30, 40):
            _r_30 += 1
        elif a in range(40, 50):
            _r_40 += 1
        elif a in range(50, 60):
            _r_50 += 1
        elif a in range(60, 70):
            _r_60 += 1
        elif a in range(70, 80):
            _r_70 += 1
        elif a in range(80, 90):
            _r_80 += 1
        elif a in range(90, 100):
            _r_90 += 1
    bool = True
    summ = 0
    ranges = [_r_9, _r_10, _r_20, _r_30, _r_40, _r_50, _r_60, _r_70, _r_80, _r_90]
    while bool:
        summ = 0
        for item in ranges: summ += item
        if summ == 0:
            bool = False
        else:
            for item in range(0, len(ranges)):
                if ranges[item] > 0:
                    print("#", end=" ")
                    ranges[item] -= 1

                else:
                    print(" ", end=" ")
            print()

