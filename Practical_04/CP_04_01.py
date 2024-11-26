# Addition of Matrices

# Input the number of matrices
num_matrices = int(input("Enter the number of matrices you want to add: "))

# Input the number of rows and columns for the matrices
X = int(input("Enter the number of rows: "))
Y = int(input("Enter the number of columns: "))

# Function to take matrix input from the user
def input_matrix(matrix_num):
    matrix = []
    print(f"Enter the entries for matrix {matrix_num} row by row:")
    for i in range(X):          
        row = []
        for j in range(Y):      
            row.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
        matrix.append(row)
    return matrix

# Store all matrices in a list
matrices = []

# Loop to input all matrices
for m in range(1, num_matrices + 1):
    matrix = input_matrix(m)
    matrices.append(matrix)

# Display all matrices
for m in range(num_matrices):
    print(f"\nMatrix {m + 1}:")
    for row in matrices[m]:
        print(row)

# Initialize the result matrix with zeros
result = [[0 for _ in range(Y)] for _ in range(X)]

# Add all matrices element by element
for matrix in matrices:
    for i in range(X):
        for j in range(Y):
            result[i][j] += matrix[i][j]

# Display the result matrix
print("\nResultant Matrix after addition:")
for row in result:
    print(row)

