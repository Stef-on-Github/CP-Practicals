

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