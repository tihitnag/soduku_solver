import random
def print_borad(puzzle):
      for r in range(9):

            for c in range(9):
                  print(puzzle[r][c],end=' ')
            print()



def find_next_empty(puzzle):
      for r in range(9):
            for c in range(9):
                  if puzzle[r][c]==0:
                        return r,c
      return None,None
def check_valid(puzzle, guess, row, col):
      row_item = puzzle[row]
      if guess in row_item:
            return False
      col_item=[]
      for i in range(9):
            col_item.append(puzzle[i][col])
            if guess in col_item:
               return  False
#to know where the first 3x3matrix we have to itrate through each row and col
            row_start=(row//3)*3
            col_start=(col//3)*3
#if itrate the in the first 3x3 grid the guess the go to the second 3x3 and guess for use for loop
            for r in range(row_start,row_start+3):
                  for c in range(col_start,col_start+3):
                       if puzzle[r][c]==guess:
                             return False
            return True


def sover_puzzle(puzzle):
      row,col=find_next_empty(puzzle)# helper function
      if row is None:
            return True
      for guess in range(1,10):
            if check_valid(puzzle, guess, row, col):
                  puzzle[row][col]=guess
                  if sover_puzzle(puzzle):
                        return True
            puzzle[row][col]=0#reset the game
      return False

if __name__ == "__main__":

            grid=[[3,0,6 ,5,0,8, 4,0,0],
                  [5,2,0, 0,0,0, 0,0,0],
                  [0,8,7, 0,0,0, 0,3,1],

                  [0,0,3, 0,1,0, 0,8,0],
                  [9,0,0, 8,6,3, 0,0,5],
                  [0,5,0, 0,9,0, 6,0,0],

                  [1,3,0, 0,0,0, 2,5,0],
                  [0,0,0, 0,0,0, 0,7,4],
                  [0,0,5, 2,0,6, 3,0,0]]
print(sover_puzzle(grid))
print_borad(grid)




