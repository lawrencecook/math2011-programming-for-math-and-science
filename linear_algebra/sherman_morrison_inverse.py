from .Matrix_Class import Matrix
from .Vector_Class import Vector 
import math

def backsub(A,b):
        n = len(A)
        x = [0] * n
        for i in reversed(range(n)):
            sum_ = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum_) / A[i][i]
        return Vector(x)

def forwsub(A,b):
    n = len(A)
    x = [0] * n
    for i in range(n):
        sum_ = sum(A[i][j] * x[j] for j in range(i))
        x[i] = (b[i] - sum_) / A[i][i]
    return Vector(x)

def frob(A):
        total = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                total += A[i][j] **2
        return math.sqrt(total)


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

def invSM(A, u, v):
    A = Matrix(A) if isinstance(A,list) else A
    Ainv = inv(A)

    vu = sum([v[0][i] * sum([Ainv[i][j] * u[j][0] for j in range(len(u))]) for i in range(len(v[0]))])
    denom = 1 + vu
    if abs(denom) < 1e-10:
        raise ValueError("Sherman-Morrison formula not applicable: denominator is zero")

    Ainu = [[sum([Ainv[i][k] * u[k][0] for k in range(len(u))]) for i in range(len(A))]]
    vTAinv = [[sum([v[0][k] * Ainv[k][j] for k in range(len(v[0]))]) for j in range(len(A[0]))]]


    correction = [[Ainu[0][i] * vTAinv[0][j] / denom for j in range(len(A[0]))] for i in range(len(A))]

    Binv = [[Ainv[i][j] - correction[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return Matrix(Binv)

A = [[0,2,1],[1,2,1],[2,7,9]]
u = [[1],[1],[1]]
v = [[1,2,3]]

B = [[A[i][j] + u[i][0] * v[0][j] for j in range(3)] for i in range(3)]
Ainv_SM = invSM(Matrix(A),u,v)
Binv_direct = inv(Matrix(B))

diff = [[Ainv_SM[i][j] - Binv_direct[i][j] for j in range(3)] for i in range(3)]
error = frob(diff)

print("Frob norm of diff:",error)

def invSM_multi(A, u_list, v_list):
    assert len(u_list) == len(v_list)
    u1,v1 = u_list[0],v_list[0]
    A1 = [[A[i][j] + u1[i][0] * v1[0][j] for j in range(len(A[0]))] for i in range(len(A))]
    
    Ainv = invSM(A1,u_list[1],v_list[1])
    return Ainv

A = [[0, 2, 1], [1, 2, 1], [2, 7, 9]]
u1 = [[1], [1], [1]]
v1 = [[1, 2, 3]]
u2 = [[1], [0], [1]]
v2 = [[0, -1, 0]]

def outer(u, v):
    return [[u[i][0] * v[0][j] for j in range(len(v[0]))] for i in range(len(u))]

uv1 = outer(u1, v1)
uv2 = outer(u2, v2)
B = [[A[i][j] + uv1[i][j] + uv2[i][j] for j in range(3)] for i in range(3)]


u_list = [u1, u2]
v_list = [v1, v2]
Binv_SM = invSM_multi(Matrix(A), u_list, v_list)

Binv_direct = inv(Matrix(B))

diff = [[Binv_SM[i][j] - Binv_direct[i][j] for j in range(3)] for i in range(3)]
error = frob(diff)
print("Frobenius norm of recursive Sherman-Morrison error:", error)

