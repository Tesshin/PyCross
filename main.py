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


def player_win(a,b):
  if b == 3:
      return('O wins')
  elif a == 3:
      return('X wins')
  else:
      return('NO win')


def check_win (x,y,table): # check for victor, returns winner or no win, work in progress
    a = 0
    b = 0

    for i in table[y]: #Checks every value in table[y] for input
        if i == 'X':
            a += 1
        elif i == 'O':
            b += 1
            
    winner = player_win(a,b)
            
    a = 0
    b = 0
    
    for i in range(3):
      if table[i][x] == 'X':
        a += 1
      elif table[i][x] == 'O':
        b += 1
        
    winner = player_win(a,b)
    
    return winner
      

def valid_input(value_x, value_y):  # test to see if user input is valid
    while True:
        try:
            value_x = int(value_x)
            value_y = int(value_y)
            if value_x >= 1 and value_y >= 1 and value_x <= grid_size and value_y <= grid_size:
                return [value_x, value_y]
                break
            elif value_x < 1:
                    print(str(value_x) + ' is too low')
                    value_x = input('x: ')
            elif value_y < 1:
                    print(str(value_y) + ' is too low')
                    value_y = input('y: ')
            elif value_x > grid_size:
                    print(str(value_x) + ' is too high')
                    value_x = input('x: ')
            elif value_y > grid_size:
                    print(str(value_y) + ' is too high')
                    value_y = input('y: ')
        except ValueError:
            print('That is not a number!')
            xy = input('x,y: ')
            value_x = xy[0]
            value_y = xy[2]

while True:  # loop for the whole program
    while True:
        grid_print(y_axis, table)  # prints grid
        xy = input('x,y: ')
        x = xy[0]
        y = xy[2]
        
        xy_values = valid_input(x, y)
        x = xy_values[0] - 1
        y = xy_values[1] - 1

        if table[y][x] == '.':
            table[y][x] = 'X'
            break  # breaks out after placing X,O

        else:
            print('That space is taken!') # check is space is taken or else the process is repeated.
    
    winner = check_win(x,y,table)
    
    if winner == 'X win' or winner == 'O win':
        break
            
    while True:
        grid_print(y_axis, table)
        xy = input('x,y: ')
        x = xy[0]
        y = xy[2]

        xy_values = valid_input(x, y)
        x = xy_values[0] - 1
        y = xy_values[1] - 1

        if table[y][x] == '.':
            table[y][x] = 'O'
            break  # breaks out after placing X,O

        else:
            print('That space is taken!') # check is space is taken or else the process is repeated.
    
    winner = check_win(x,y,table)
    
    if winner == 'X win' or winner == 'O win':
        break



    
    
        
