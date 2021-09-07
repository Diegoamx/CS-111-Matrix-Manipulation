#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Matrix Operations  
#
# Computer Science 111   
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

def mult_row(matrix, r, m):
    """that multiplies row r of the specified matrix by the 
        specified multiplier m.
        inputs: matrix is a rectangular 2-D list of numbers
                r is a row in matrix
                m is an integer
    """
    for c in range(len(matrix[0])):
        matrix[r][c] *= m
    return matrix

def add_row_into(matrix, source, dest):
    """takes the specified 2-D list matrix and adds each element
       of the row with index source (the source row) to the 
       corresponding element of the row with index dest 
       (the destination row).
       inputs: matrix is a rectangular 2-D list of numbers
               source is a row in matrix
               dest is a row in matrix
    """
    for c in range(len(matrix[0])):
        matrix[dest][c] += matrix[source][c]
    return matrix
    
def add_mult_row_into(matrix, m, source, dest):
    """takes the specified 2-D list matrix and adds each element
       of row source (the source row), multiplied by m, to the 
       corresponding element of row dest (the destination row).
       inputs: matrix is a rectangular 2-D list of numbers
               source is a row in matrix
               dest is a row in matrix
               m is an integer
    """
    for c in range(len(matrix[0])):
        matrix[dest][c] += matrix[source][c] * m
    return matrix

def transpose(matrix):
    """takes the specified 2-D list matrix and creates and 
       returns a new 2-D list that is the transpose of matrix.
       inputs: matrix is a rectangular 2-D list of numbers
    """
    tmatrix =[[r[c] for r in matrix] for c in range(len(matrix[0]))] 
    
    return tmatrix

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)
 ## add code to handle the other options here
        elif choice == 2:
            row = int(input('Enter a row number: '))
            multiplier = int(input('Enter a multiplier: '))
            matrix = mult_row(matrix, row, multiplier)
        elif choice == 3:
            sourcer = int(input('Enter a source row: '))
            destination = int(input('Enter a row destination: '))
            matrix = add_row_into(matrix, sourcer, destination)
        elif choice == 4:
            sourcer = int(input('Enter a source row: '))
            destination = int(input('Enter a row destination: '))
            multiplier = int(input('Enter a multiplier: '))
            matrix = add_mult_row_into(matrix, multiplier, sourcer, destination)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
