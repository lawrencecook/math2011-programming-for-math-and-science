from .Vector_Class import Vector
from .Matrix_Class import Matrix 

def QR(A):
        m,n = len(A), len(A[0])
        print(m,n)
        Q = [[0 for j in range(n)] for i in range(m)]
        R = [[0 for j in range(n)] for i in range(n)]
        for j in range(n):
            aj = Vector([A[_][j] for _ in range(m)])
            print(aj)
            wj = aj.copy()
            for k in range(j):
                qk = Vector([Q[_][k] for _ in range(m)])
                R[k][j] = Vector.dot(aj,qk)
                wj = wj - R[k][j] * qk
            norm_wj = Vector.dot(wj,wj)**0.5
            if norm_wj < 1e-10:
                print(f"Column {j} is lineraly dependent - skiping")
                continue
            qj = wj/norm_wj
            for _ in range(m):
                Q[_][j] = qj[_]
            R[j][j] = Vector.dot(aj,qj)
        return Matrix(Q),Matrix(R)

A = [[1,3],[2,7]]
Q, R = QR(A)

print("Q =",Q)
print("R =",R)

A = [[1,1],[2,-1],[-2,4]]
Q, R = QR(A)

print("Q =",Q)
print("R =",R)

A = [[0,1,2,3]]
Q, R = QR(A)

print("Q =",Q)
print("R =",R)

A = [[1,2,1],[1,0,1],[1,-1,3],[1,1,0]]
Q,R = QR(A)

print("Q =",Q)
print("R =",R)

