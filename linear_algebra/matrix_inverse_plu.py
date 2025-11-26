from copy import deepcopy
from .matrix_utilities2 import Matrix
from .Vector_Class import Vector
def backsub(U,b):
    n = len(U)
    x = [0] *n
    for i in reversed(range(n)):
        sum_ = sum(U[i][j] * x[j] for j in range(i +1,n))
        x[i] = (b[i] - sum_) / U[i][i]
    return x

def forwsub(A,b):
    n = len(A)
    x = [0] * n 
    for i in range(n):
        sum_ = sum(A[i][j] * x[j] for j in range(i))
        x[i] = (b[i] - sum_) / A[i][i]
    return x


def getPLU(A):
    A = [row[:] for row in A]
    n = len(A)
    P = [[float(i==j) for j in range(n)] for i in range(n)]
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        max_row = max(range(i,n) , key=lambda r: abs(A[r][i]))
        if abs(A[max_row][i]) < 1e-12:
            raise ValueError("Matrix is singular")
    
        if i != max_row:
            A[i],A[max_row] = A[max_row],A[i]
            P[i],P[max_row] = P[max_row],P[i]
            L[i][:i], L[max_row][:i] = L[max_row][:i], L[i][:i]

        L[i][i] = 1.0

        for j in range(i,n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i +1,n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) /U[i][i]

    return Matrix(P), Matrix(L), Matrix(U)

def det(A):
    if len(A.data) != len(A.data[0]):
        raise ValueError("Function is only defined for square matricies")

    _, U = getLU(A.data)
    product = 1
    for i in range(len(U.data)):
        product *= U.data[i][i]
    return product

def inv(A):
    if len(A.data) != len(A.data[0]):
        raise ValueError("Function is only defined for square matricies")

    n = len(A)
    P,L,U = getPLU(A.data)
    I = [[float(i == j) for j in range(n)] for i in range(n)]

    inverse_cols = []

    for col in range(n):
        b = [sum(P.data[i][k] * I[k][col] for k in range(n)) for i in range(n)]
        y = forwsub(L.data ,b)
        x = backsub(U.data ,y)
        inverse_cols.append(x)

    
    inverse_data = [[inverse_cols[j][i] for j in range(n)] for i in range(n)]
    return Matrix(inverse_data)

A = Matrix([[3,2,2],[3,14,12],[9,10,9]])
A_inv = inv(A)
print(f"Inverse of A:{A_inv}")

C = Matrix([[2,2,5,2],[2,1,1,1],[0,2,8,1],[-2,0,5,2]])
C_inv = inv(C)
print(f"Inverse of C:{C_inv}")

#This Matrix B is not invertible
#B = Matrix([[1,2,3],[4,5,13],[3,-3,12]])
#B_inv = inv(B)
#print(f"Inverse of B:{B_inv}")
print("The Matrix B is not invertible")

