class Solver:
    NUMBERS = [i for i in range(1,10)]

    def __init__(self,gameboard):
        self.board = gameboard.board
    
    def find_empty_square(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
    
    def is_valid(self,row, col, number):
        # check row
        for val in self.board[row]:
            if val == number:
                return False  

        # check col    
        for val in range(9):
            if self.board[val][col] == number:
                return False 
        
        #check cell
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == number:
                    return False
              
        return True
    

    def solve(self):
        if (empty_square := self.find_empty_square()) is None:
            return True
        else:
            for number in self.NUMBERS:
                if self.is_valid(empty_square[0], empty_square[1], number):
                    self.board[empty_square[0]][empty_square[1]] = number
                    if self.solve():
                        return True
                    else:
                        self.board[empty_square[0]][empty_square[1]] = 0

            return False