from linear_algebra.matrix_utilities2 import Matrix, Vector, perm2mat, frob, forwsub, backsub
import math

def lu(A):
    A = [row[:] for row in A]
    n = len(A)
    p = list(range(n))

    for k in range(n):
        max_row = max(range(k,n), key=lambda i: abs(A[i][k]))
        A[k], A[max_row] = A[max_row], A[k]
        p[k], p[max_row] = p[max_row], p[k]

        for i in range(k + 1, n):
            A[i][k] /= A[k][k]
            for j in range(k + 1,n):
                A[i][j] -= A[i][k] * A[k][j]

    L = [[1 if i==j else A[i][j] if i>j else 0 for j in range(n)] for i in range(n)]
    U = [[A[i][j] if i<= j else 0 for j in range(n)] for i in range(n)]
    P = perm2mat([i + 1 for i in p])

    PA = [[sum(P[i][k] * A[k][j] for k in range(n)) for j in range(n)] for i in range (n)]
    LU = [[sum(L[i][k] * U[k][j] for k in range(n)) for j in range(n)] for i in range (n)]
    err = frob(Matrix([[PA[i][j] - LU[i][j] for j in range(n)] for i in range(n)]))

    return Matrix(L), Matrix(U), Matrix(P), err


def solve(A,b):
    L,U,P, _ = lu(A)

    Pb = [sum(P[i][j] * b[j] for j in range(len(b))) for i in range(len(b))]
    y = forwsub(L,Pb)
    x = backsub(U,y)
    x = x[::-1]
    Ax = [sum(A[i][j] * x[::-1][j] for j in range(len(x))) for i in range(len(A))]
    error = math.sqrt(sum((Ax[i] - b[i])**2 for i in range(len(b))))

    return x, error

#10.1 Solution
A = Matrix([[1,-7,1],[0,2,-1],[0,0,1]])
b = [1,4,5]

x, error = solve(A,b)

print("Solution 10.1",x)
print("error:",error)

# Polynomial system for sum of cubes
A_poly = Matrix([[1,1,1,1,1],[1,2,4,8,16],[1,3,9,64,256],[1,4,16,64,256],[1,5,25,125,625]])
b_poly = [1,9,36,100,225]

coeffs, error = solve(A_poly,b_poly)
print("Coefficients x0 to x4:", coeffs)

print("This is the error:",error)

#Polynomial system for sum of 4th powers
A_poly4 = Matrix([[1,1,1,1,1,1],[1,2,4,18,16,32],[1,3,9,27,81,243],[1,4,16,64,256,1024],[1,5,25,125,625,3125],[1,6,36,216,1296,7776]])
b_poly4 = [1,7,98,354,979,2275]
coeffs_4, error_4 = solve(A_poly4,b_poly4)
print("coeff x0 to x5:", coeffs_4)

print("This is the error:", error_4)
