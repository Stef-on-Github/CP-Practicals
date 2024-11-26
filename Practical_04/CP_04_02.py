#Multiplcation of the Matrices

# Input the number of matrices
num_matrices = int(input("Enter the number of matrices you want to multiply: "))

# Input the dimensions for the first matrix
A_rows = int(input("Enter the number of rows for the first matrix: "))
A_cols = int(input("Enter the number of columns for the first matrix: "))

# Function to input matrix elements from the user
def input_matrix(matrix_num, rows, cols):
    matrix = []
    print(f"Enter the entries for matrix {matrix_num} row by row:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
        matrix.append(row)
    return matrix

# Store all matrices
matrices = []

# Input the first matrix
matrix = input_matrix(1, A_rows, A_cols)
matrices.append(matrix)

# Now we need to input remaining matrices and check compatibility for multiplication
for m in range(2, num_matrices + 1):
    # For the m-th matrix, input rows and columns
    B_rows = int(input(f"Enter the number of rows for matrix {m}: "))
    B_cols = int(input(f"Enter the number of columns for matrix {m}: "))
    
    # Check if the current matrix is compatible with the previous matrix for multiplication
    if A_cols != B_rows:
        print(f"Matrix multiplication cannot be performed because the number of columns of matrix {m-1} "
              "is not equal to the number of rows of matrix {m}.")
        exit()

    # Input the m-th matrix
    matrix = input_matrix(m, B_rows, B_cols)
    matrices.append(matrix)

    # Update dimensions for the next matrix multiplication
    A_rows = B_rows
    A_cols = B_cols

# Display the matrices entered by the user
for m in range(num_matrices):
    print(f"\nMatrix {m + 1}:")
    for row in matrices[m]:
        print(row)

# Function to multiply two matrices
def multiply_matrices(A, B):
    # Get the dimensions of A and B
    A_rows = len(A)
    A_cols = len(A[0])
    B_rows = len(B)
    B_cols = len(B[0])

    # Check if multiplication is possible
    if A_cols != B_rows:
        print("Matrix multiplication is not possible due to incompatible dimensions.")
        return None

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(B_cols)] for _ in range(A_rows)]

    # Perform matrix multiplication
    for i in range(A_rows):
        for j in range(B_cols):
            for k in range(A_cols):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Multiply all matrices
result_matrix = matrices[0]
for i in range(1, num_matrices):
    result_matrix = multiply_matrices(result_matrix, matrices[i])

# Display the result of multiplication
print("\nResultant Matrix after multiplication:")
for row in result_matrix:
    print(row)
