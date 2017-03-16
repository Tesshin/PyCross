table = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'], ]  # Gets the grid set up

x_axis = 0  # sets x_axis starting point
y_axis = 0  # sets y_axis starting point

grid_size = 5  # sets grid size, used to detemine maximum x & y values.


def grid_print(y_axis, table):  # Prints the grid
    print('  1 2 3 4 5')
    for i in table:
        y_axis += 1
        print(str(y_axis), end=' ')
        for x in i:
            print(x, end=' ')
        print('')


def check_win():  # check for victor, returns winner or no win, wip
    # for i in
    a = 0
    b = 0

    for i in table[y]:
        if i == 'X':
            a += 1
        elif i == 'O':
            b += 1

    if b == 3:
        return('X wins')
    if a == 3:
        return('O wins')


def test(value_x, value_y):  # test to see if user input is valid
    while True:
        try:
            value_x = int(value_x)
            if value_x >= 1 and value_x <= grid_size:
                break

            elif value_x < 1:
                print(str(value_x) + ' is too low')
                value_x = input('x,y: ')

            elif value_x > grid_size:
                print(str(value_x) + ' is too high')
                value_x = input('x,y: ')

        except ValueError:
            print('That is not a number!')
            value_x = input('x,y: ')

        try:
            value_y = int(value_y)
            if value_y >= 1 and value_y <= grid_size:
                break
            elif value_y < 1:
                print(str(value_y) + ' is too low')
                value_y = input('x,y: ')
            elif value_y > grid_size:
                print(value_y + ' is too high')
                value_y = input('x,y: ')
        except ValueError:
            print('That is not a number!')
            value_y = input('x,y: ')

while True:  # loop for the whole program
    grid_print(y_axis, table)  # prints grid

    while True:
        xy = input('x,y: ')
        x = xy[0]
        y = xy[2]
        
        test(x, y)
        x = int(x) - 1
        y = int(y) - 1

        if table[y][x] == '.':
            table[y][x] = 'X'
            break  # breaks out after placing X,O

        else:
            print('That space is taken!')
            # check is space is taken or else the process is repeated.

    while True:
        grid_print(y_axis, table)

        xy = input('x,y: ')
        xy_list = xy.split()
        x = xy_list[0][0]
        y = xy_list[0][2]

        test(x, 'x')
        x = int(x) - 1

        test(y, 'y')
        y = int(y) - 1

        if table[y][x] == '.':
                table[y][x] = 'O'
                break  # breaks out after placing X,O

        else:
            print('That space is taken!')
            # check is space is taken or else the process is repeated.
