from copy import deepcopy

ask = """1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit
Your choice: > """

class Matrices:

    choice = input(ask).strip()

    def __init__(self):

        self.choice = Matrices.choice
        self.fn, self.fm  = 0, 0
        self.sn, self.sm = 0, 0
        self.constant = 0
        self.first_matrix = []
        self.second_matrix = []
        self.result = []
        self.int_matrix = []
        self.answer = 0
        self.simple_determinant = 0
        self.new_matrix = []
        self.solo = 0
        self.adjoint = []


    def two_matrices(self): # Questions
        try:
            fn, fm = input("Enter size of first matrix: ").split()
            self.fn, self.fm = int(fn), int(fm)
            print("Enter first matrix:")
            for _ in range(self.fn):
                numbers = input("").split()
                if len(numbers) == self.fm:
                    self.first_matrix.append(numbers)

            sn, sm = input("Enter size of second matrix: >").split()
            self.sn, self.sm = int(sn), int(sm)
            print("Enter second matrix:")
            for _ in range(self.sn):
                numbers = input("> ").split()
                if len(numbers) == self.sm:
                    self.second_matrix.append(numbers)

            return True
        except:
            return False
    
    def matrix_constant(self): # Questions
        try:
            fn, fm = input("Enter size of matrix: >").split()
            self.fn, self.fm = int(fn), int(fm)
            print("Enter matrix:")
            for _ in range(self.fn):
                numbers = input("> ").split()
                if len(numbers) == self.fm:
                    self.first_matrix.append(numbers)
          
            constant = input("Enter constant: > ")
            self.constant = float(constant)
            return True
        except:
            return False
    
    def matrix_4_tropose(self): # Questions
        try:
            fn, fm = input("Enter matrix size: > ").split()
            self.fn, self.fm = int(fn), int(fm)
            print("Enter first matrix:")
            for _ in range(self.fn):
                numbers = input("> ").split()
                if len(numbers) == self.fm:
                    self.first_matrix.append(numbers)
            return True
        except:
            return False

    def det_matrix(self): # Questions
        try:
            fn, fm = input("Enter matrix size: > ").split()
            self.fn, self.fm = int(fn), int(fm)
            print("Enter matrix:")
            for _ in range(self.fn):
                numbers = input("> ").split()
                if len(numbers) == self.fm:
                    self.first_matrix.append(numbers)
            if "." in self.first_matrix[0][0]:
                self.int_matrix = [[float(n) for n in i]for i in self.first_matrix]
            else:
                self.int_matrix = [[int(n) for n in i]for i in self.first_matrix]

            return True
        except:
            return False

    # Function to print The Matrix
    def printer(self, function):
        print("The result is:")
        row = self.fn
        if self.choice == "3":
            column = self.sm
        else:
            column = self.fm
        for j in range(row):
            for i in range(column):
                print(function[j][i], end= " ")
            print("\r")
        print()

############################### OPERATIONS ####################################

    # Addition Matrix
    def addition(self):
        if self.two_matrices():           
            if self.fn == self.sn and self.fm == self.sm:
                for i in range(self.fn):
                    new = []
                    for j in range(self.fm):
                        if "." in self.first_matrix[i][j] :
                            new.append(float(self.first_matrix[i][j]) + float(self.second_matrix[i][j]))
                        else:
                            new.append(int(self.first_matrix[i][j]) + int(self.second_matrix[i][j]))
                    self.result.append(new)
                self.printer(self.result)
            else:
                print("The operation cannot be performed.")

    # Matrix By Constant
    def matrix_by_constant(self): 
        if self.matrix_constant():
            for i in range(self.fn):
                new = []
                for j in range(self.fm):
                    new.append(float(self.first_matrix[i][j]) * self.constant)
                self.result.append(new)
            self.printer(self.result)
        else:
            print("Please make sure your values are correct!")

    # Multiplication : Matrix by Matrix 
    def matrix_by_matrix(self):         
        if self.two_matrices():
            if self.fm == self.sn:
                def multiplication(index, matrix1, matrix2):
                    new = []
                    for i in range(self.sm):
                        total = 0
                        for j in range(self.sn):
                            if "." in matrix1[index][j]:
                                total += float(matrix1[index][j]) * float(matrix2[j][i]) 
                            else:
                                total += int(matrix1[index][j]) * int(matrix2[j][i])                       
                        new.append(total)
                    return new

                for i in range(self.fn):
                    lis = multiplication(i, self.first_matrix, self.second_matrix)
                    self.result.append(lis)
                self.printer(self.result)


    def transpose_matrix(self):
        ask = input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice:")
        if self.matrix_4_tropose():
            print("The result is:")

            if ask == "1": # Main Diagonal
                for i in range(self.fn):
                    for j in range(self.fm):
                        print(self.first_matrix[j][i], end=" ")
                    print("\r")

            elif ask == "2": # Side Diagonal
                for i in range(self.fn-1, -1, -1):
                    for j in range(self.fm-1, -1, -1):
                        print(self.first_matrix[j][i], end=" ")
                    print("\r")

            elif ask == "3": # Vertical Line
                for i in range(self.fn):
                    for j in range(self.fm-1, -1, -1):
                        print(self.first_matrix[i][j], end=" ")
                    print("\r")

            elif ask == "4": # Horizontal Line
                for i in range(self.fn-1, -1, -1):
                    for j in range(self.fm):
                        print(self.first_matrix[i][j], end=" ")
                    print("\r")

    # Determinant calculation Starts

    def determinant(self):
        if self.det_matrix():

            def smaller_matrix(original_matrix, row, column):
                self.new_matrix = deepcopy(original_matrix)
                self.new_matrix.remove(original_matrix[row])
                for i in range(len(self.new_matrix)):
                    self.new_matrix[i].pop(column)
                return self.new_matrix

            def inside_determinant(matrix):
                num_rows = len(matrix)
                for row in matrix:
                    if len(row) != num_rows:
                        print("Not a square martix.")
                        return None
                if len(matrix) == 1:
                    self.solo = matrix[0][0]
                    return self.solo
                elif len(matrix) == 2:
                    self.simple_determinant = matrix [0][0] * matrix [1][1] \
                                        - matrix [1][0] * matrix [0][1]
                    return self.simple_determinant
                else:
                    #cofactor expansion
                    det = 0
                    num_columns = num_rows
                    for i in range(num_columns):
                        answer = (-1) ** i * matrix[0][i] \
                                 * inside_determinant(smaller_matrix(matrix, 0, i))
                        det += answer 
                        new = []                                               
                        for j in range(num_rows):
                            minor = ((-1) ** (i + j)) * inside_determinant(smaller_matrix(matrix, i, j))
                            new.append(minor)
                        if len(new) == self.fn:
                            self.adjoint.append(new)
                        # return self.adjoint
                    return det
                return self.adjoint
            return inside_determinant(self.int_matrix)

    # Determinant calculation Ends

    # Inverse Matrix
    def inverse_matrix(self):
        det = self.determinant()
        if det != 0:
            print("The result is:")
            for i in range(self.fn):
                for j in range(self.fn):
                    inside = (1 / (det)) * self.adjoint[j][i] 
                    if inside == 0:
                        inside = 0
                    b = str(inside).find(".")
                    print(str(inside)[:b+3], end=" ")
                print("\r")
        else: 
            print("This matrix doesn't have an inverse.")

    #Exit
    def exit(self):
        quit()

########### Final step printing results ###########

    def action(self):
        
        while self.choice != "0":

            if self.choice == "1":
                self.addition()

            elif self.choice == "2":
                self.matrix_by_constant()
            
            elif self.choice == "3":
                self.matrix_by_matrix()

            elif self.choice == "4":
                self.transpose_matrix()
            
            elif self.choice == "5":                
                print(self.determinant())

            elif self.choice == "6":
                self.inverse_matrix()

            elif self.choice == "0":
                self.exit()

            else:
                print("Please choose from the given choices!")
            self.choice = input(ask).strip()
            self.first_matrix = []
            self.second_matrix = []
            self.result = []
            self.int_matrix = []
            self.answer = 0
            self.simple_determinant = 0
            self.new_matrix = []
            self.solo = 0
            self.adjoint = []

###### Call the Class ######

Matrices().action()


