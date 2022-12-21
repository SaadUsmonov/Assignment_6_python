import array as array


def task_one(rows, cols):
    mat = [[0 for _ in range(cols)] for _ in range(rows)]
    matter = list()
    for row in range(rows):
        for column in range(cols):
            mat[row][column] = int(input(f'Enter the number for sell [{row}][{column}]: '))
            if row == 0:
                matter.append(0)

    for row in range(rows):
        sum_row = 0
        for column in range(cols):
            sum_row += mat[row][column]
            matter[column] += mat[row][column]
            print(mat[row][column], end=" ")
        print(sum_row, end="")
        print()
    for item in matter: print(item, end=" ")