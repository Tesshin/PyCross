# Bugs:
# Check win doesnt work properly.


table = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.'],] # Gets the grid set up

x_axis = 0 # sets x_axis starting point
y_axis = 0 # sets y_axis starting point

grid_size = 3 # sets grid size, used to detemine maximum x & y values.

winner = 'NO win'
 
def grid_print (y_axis,table): # Prints the grid
    print('  1 2 3')
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
      
    
      
    

def test (x,y): # test to see if user input is valid
    while True:
        try:
            x = int(x)
            if x >= 1 and x <= grid_size:
                break
            
            elif x < 1:
                print(x,'is too low')
                x = input(y + ': ')
                
            elif x > 3:
                print(x,'is too high')
                x = input(y + ': ')
                
        except ValueError:
            print('That is not a number!')
            x = input(y + ': ')
        


while True: # loop for the whole program
    grid_print(y_axis,table) #prints grid

    while True:
        x = input('x: ')
        test(x,'x')
        x = int(x) - 1

                
        y = input('y: ')
        test(y,'y')
        y = int(y) - 1

        if table[y][x] == '.':
            table[y][x] = 'X'
            break # breaks out after placing X,O 

        else:
            print('That space is taken!') # check is space is taken or else the process is repeated.
    
    winner = check_win(x,y,table)
    
    if winner == 'X win' or winner == 'O win':
        break
            
    while True:
        grid_print(y_axis,table)

        x = input('x: ')
        test(x,'x')
        x = int(x) - 1

                
        y = input('y: ')
        test(y,'y')
        y = int(y) - 1

        if table[y][x] == '.':
                table[y][x] = 'O'
                break # breaks out after placing X,O 

        else:
            print('That space is taken!') # check is space is taken or else the process is repeated.
    
    winner = check_win(x,y,table)
    
    if winner == 'X win' or winner == 'O win':
        break



    
    
        
