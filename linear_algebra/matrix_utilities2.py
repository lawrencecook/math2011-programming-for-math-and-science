from collections import UserList
import numpy as np
import math 
class Vector(UserList):
    def __str__(self):
        s = str(self.data)
        return '(' + s[1:-1] + ')'

    def __add__(self,other):
        return Vector([a + b for a, b in zip(self,other)])

    def __sub__(self,other):
        return Vector([a - b for a,b in zip(self,other)])

    def __mul__(self,other):
        return Vector([other*a for a in self])
    
    __rmul__ = __mul__

    def __truediv__(self,other):
        return Vector([other/a for a in self])

class Matrix:
    def __init__(self,data):
        self.data = data

    def __getitem__(self,idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

    def format(self,row):
        s = ' '
        for x in row:
            s = s + "{: 10.4}".format(float(x)) + ' '
        return s[0:-1]

    def __str__(self):
        if not self.data:
            return "[Empty Matrix]"
        lines = [f"\u2308{self.format(self.data[0])}\u2309"]
        for row in self.data[1:-1]:
            lines.append(f"|{self.format(row)}|")
        if len(self.data) > 1:
            lines.append(f"\u230A{self.format(self.data[-1])}\u230B")
        return "\n".join(lines)

    def __add__(self,other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Incompatible dimensions")
        return Matrix([[self.data[i][j] + other[i][j] for j in range(len(self.data[0]))] for i  in range(len(self.data))])
    def __mul__(self,other):
        if type(other) in {int,float}:
            return Matrix([[other * val for val in row] for row in self.data])
        elif type(other) == Vector:
            if len(self.data[0]) != len(other):
                raise ValueError("Incompatible dimensions")
            return Vector([sum(row[j] * other[j] for j in range(len(other))) for row in self.data])
        elif type(other) == Matrix:
            if len(self.data[0]) != len(other.data):
                raise ValueError("Incompatible dimensions")
            result = []
            for row in self.data:
                new_row = []
                for col in zip(*other.data):
                    new_row.append(sum(r*c for r,c in zip(row,col)))
                result.append(new_row)
            return Matrix(result)
        else:
            raise TypeError("Imcompatiabnle type for multiplcation")


def __rmul__(self,other):
        return self.__mul__(other)

def inverse(self):
        inv = np.linalg.inv(np.array(self.data))
        return Matrix(inv.tolist())
#8
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

A = Matrix([[2,1,3],[0,5,1],[0,0,3]])
b = Vector([1,4,6])
x = backsub(A,b)
print("3a:" , x)

A = Matrix([[1,0,0,0],[2,1,0,0],[1,-1,3,0],[0,-4,1,1]])
b = Vector([2,-1,4,1])
x = forwsub(A,b)
print("3b:" , x)

L = Matrix([[1,0,0] , [-1,1,0],[2,1,1]])
U = Matrix([[1,2,2], [0,3,1],[0,0,-1]])
b = Vector([2,1,1])
def lusolve(L,U,b):
    y = forwsub(L,b)
    x = backsub(U,y)
    return x

x = lusolve(L,U,b)
print("#5a Solution = ", x)

b = Vector([1,0,2])
x = lusolve(L,U,b)
print("#5b Solution = ",x)

b = Vector([5,-1,4])
x = lusolve(L,U,b)
print("#5c Solution = ",x)

#9
def perm2mat(p):
    n = len(p)
    P = np.zeros((n,n))
    for i in range(n):
        P[i, p[i] - 1] = 1
    return P
p = [3,4,1,5,2]
q = [1,3,2,5,4]
P = perm2mat(p)
Q = perm2mat(q)

#10
def getLU(A):
    m = len(A)
    n = len(A[0])

    L = [[1 if i==j else 0 for j in range(m)] for i in range(m)]
    for i in range(2,m):
        for j in range(n):
            L[i][j] = A[i][j]
    U = [[A[i][j] if i<=j else 0 for j in range(n)] for i in range(m)]

    return Matrix(L),Matrix(U)
A = Matrix([[-1,3],[0,4],[1,5],[2,6]])
B = Matrix([[-1,1,3],[0,2,4]])

L, U = getLU(A)

print("L =", L)
print("U =", U)

L, U = getLU(B)
print("L =", L)
print("U =", U)

#11
def frob(A):
    total = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            total += A[i][j] **2
    return math.sqrt(total)

def Transpose(A):
    return Matrix([[A.data[j][i] for j in range(A.rows)] for i in range(A.columns)])
def dot(x,y):
    return sum([x[a] * y[a] for a in range(len(x))])

#QR Factorization
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
            R[k][j] = dot(aj,qk)
            wj = wj - R[k][j] * qk
        qj = wj/(dot(wj,wj))**0.5
        for _ in range(m):
            Q[_][j] = qj[_]
        R[j][j] = dot(aj,qj)
    return Matrix(Q),Matrix(R)

A = Matrix([[1,2,1],[1,0,1],[1,-1,3],[1,1,0]])

print(A)
Q,R = QR(A)
print(Q)
print(R)

