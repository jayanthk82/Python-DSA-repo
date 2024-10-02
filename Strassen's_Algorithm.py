import numpy as np

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(A, B):
    if len(A) == 1:
        return A * B
    
    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    M1 = strassen(A11 + A22, B11 + B22)  
    M2 = strassen(A21 + A22, B11)       
    M3 = strassen(A11, B12 - B22)        
    M4 = strassen(A22, B21 - B11)       
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)  
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))

def next_power_of_2(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def pad_matrix(matrix, new_size):
    padded_matrix = np.zeros((new_size, new_size))
    padded_matrix[:matrix.shape[0], :matrix.shape[1]] = matrix
    return padded_matrix

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

n = max(A.shape[0], B.shape[0])
new_size = next_power_of_2(n)

A_padded = pad_matrix(A, new_size)
B_padded = pad_matrix(B, new_size)

C_padded = strassen(A_padded, B_padded)

C = C_padded[:A.shape[0], :B.shape[1]]

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nProduct of A and B using Strassen's Algorithm:")
print(C)

