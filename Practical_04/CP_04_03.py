# Input the number of rows and columns for the matrix
X = int(input("Enter the number of rows: "))
Y = int(input("Enter the number of columns: "))

# Function to take matrix input from the user
def input_matrix():
    matrix = []
    print("Enter the entries for the matrix row by row:")
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(int(input(f"Enter element [{i+1},{j+1}]: ")))
        matrix.append(row)
    return matrix

# Input the matrix
matrix = input_matrix()

# Display the original matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Compute the transpose of the matrix
transpose = [[matrix[i][j] for i in range(X)] for j in range(Y)]

# Display the transposed matrix
print("\nTransposed Matrix:")
for row in transpose:
    print(row)
