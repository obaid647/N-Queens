import random

class nQueensCSP:
    def __init__(self, n):
        # n-queens is represented by a 1D list where each index is the column and the value at that index/column is the row that contains the queen
        #e.g. [0,2,1]
        #at column 0 the queen is in row 0
        #at column 1 the queen is in row 2
        #at column 2 the queen is in row 1
        self.variables = [random.randint(0,n-1) for i in range (n) ]


    def conflicts(self, col):
        #col 
        count = 0
        row = self.variables[col]
        n = len(self.variables)

        for col2 in range(n):
            row2 = self.variables[col2]
            if row2 == row and col2 != col:
                count+=1
            if abs(row2 - row) == abs(col2 - col) and col2!= col:
                count+=1
        return count
    def is_valid_solution(self):
        n = len(self.variables)
        for col in range(n):
            if self.conflicts(col) > 0:
                return False
        return True
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
    
csp = nQueensCSP(8)


print(csp.variables)
num = csp.conflicts(0)
print(num)
print_board(csp.variables)
solution = csp.is_valid_solution()
print("Is valid solution: ",solution)

