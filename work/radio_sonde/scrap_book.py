"""
Write a function array_mult that takes two two-dimensional 
arrays and performs a matrix multiplication, return a new 
two-dimensional array. Each array should be represented as a 
list of lists, i.e., as a list of rows, as discussed earlier. 
For example,

>>> M1 = [[1, 2, 3], [-2, 3, 7]]
>>> M2 = [[1,0,0],[0,1,0],[0,0,1]]
>>> array_mult(M1, M2)
[[1, 2, 3], [-2, 3, 7]]

>>> M3 = [[1], [0], [-1]]
>>> array_mult(M1, M3)
[[-2], [-9]]
"""



# Define matrix A (2x3)
M1 = [[1, 2, 3], [-2, 3, 7]]

# Define matrix B (3x3)
M2 = [[1,0,0],[0,1,0],[0,0,1]]

# Get dimensions
rows_M1 = len(M1)
cols_M1 = len(M1[0])
rows_M2 = len(M2)
cols_M2 = len(M2[0])

# Check if matrices can be multiplied
if cols_M1 != rows_M2:
    print("Error: Cannot multiply, incompatible dimensions.")
    result = None
else:
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_M2)] for _ in range(rows_M1)]

    # Matrix multiplication logic
    for i in range(rows_M1):
        for j in range(cols_M2):
            for k in range(cols_M1):
                result[i][j] += M1[i][k] * M2[k][j]

    # Display result
    print("Matrix A x B =")
    for row in result:
        print(row)
