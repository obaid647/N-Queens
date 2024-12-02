import random
from collections import Counter

class nQueensCSP:
    def __init__(self, n):
        
        # n-queens is represented by a 1D list where each index is the column and the value at that index/column is the row that contains the queen
        #e.g. [0,2,1]
        #at column 0 the queen is in row 0
        #at column 1 the queen is in row 2
        #at column 2 the queen is in row 1
        
        self.n = n
        self.variables = [random.randint(0,n-1) for i in range (n) ]
        
        # list to keep track of conflicts in each row
        self.row_conflicts = Counter(self.variables)  
        
        # list to keep track of conflicts in each right diagonal (top left to bottom right)
        # row-col will be the same number for each element that is in the same diagonal
        # the min number that row-col could be is 0 - (n-1) = -(n-1) and the max number is (n-1) - 0 = n-1
        # so the range is -(n-1) to n-1 which is 2*n-1 (the size of this list) 
        self.rdiag_conflicts = Counter(row - col for col, row in enumerate(self.variables))
        
        # list to keep track of conflicts in each left diagonal (top right to bottom left)
        self.ldiag_conflicts = Counter(row + col for col, row in enumerate(self.variables))
        
        self.conflicted_queens = {
            col for col in range(n) if self.conflicts(col) > 0
        }

        
        # CONFLICT LISTS ARE ALL CORRECT 
        # print("row_conflicts list:", self.row_conflicts) 
        # print("rdiag_conflicts list:", self.rdiag_conflicts) 
        # print("ldiag_conflicts list:", self.ldiag_conflicts) 

    def conflicts(self, col):

        row = self.variables[col]
        rdiag_index = row - col
        ldiag_index = row + col

        return (
            self.row_conflicts[row] - 1 +
            self.ldiag_conflicts[ldiag_index] - 1 +
            self.rdiag_conflicts[rdiag_index] - 1
        )

    def is_valid_solution(self):
        return len(self.conflicted_queens) == 0

    
    def move_queen(self, col, new_row):
        
        old_row = self.variables[col]
        rdiag_old = old_row - col
        ldiag_old = old_row + col
        rdiag_new = new_row - col
        ldiag_new = new_row + col

        # Update conflicts by removing old position
        self.row_conflicts[old_row] -= 1
        self.rdiag_conflicts[rdiag_old] -= 1
        self.ldiag_conflicts[ldiag_old] -= 1

        # Move queen
        self.variables[col] = new_row

        # Update conflicts with new position
        self.row_conflicts[new_row] += 1
        self.rdiag_conflicts[rdiag_new] += 1
        self.ldiag_conflicts[ldiag_new] += 1

        # Update conflicted queens
        if self.conflicts(col) > 0:
            self.conflicted_queens.add(col)
        else:
            self.conflicted_queens.discard(col)


def print_board(state):
        n = len(state)
        for row in range(n):
            row_string = ""
            for col in range(n):  
                if state[col] == row:
                    row_string += "Q "
                else:
                    row_string += ". "
            print(row_string.strip()) 
    




