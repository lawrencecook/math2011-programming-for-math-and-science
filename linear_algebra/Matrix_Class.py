from .Vector_Class import Vector
import numpy as np

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

    def column(x):
        if type(x) != Vector:
            raise TypeError("Input must be a Vector")
        return Matrix([[val] for val in x])

    def eye(n):
        return Matrix([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    def zeroes(m,n):
        return Matrix([[0 for _ in range(n)] for _ in range(m)])

    def ones(m,n):
        return Matrix([[1 for x in range(n)] for x in range(m)])

    def flipud(A):
        if type(A) != Matrix:
            raise TypeError("Input must be a Matrix")
        return Matrix(A.data[::-1])

    def fliplr(A):
        if type(A) != Matrix:
            raise TypeError("Input must be a Matrix")
        return Matrix([row[::-1] for row in A.data])

    def diag(v, p=0):
        if type(v) != Vector:
            raise TypeError("Input must be a Vector")
        n = len(v)
        size = n + abs(p)
        mat = [[0 for i in range(size)] for i in range(size)]

        for t in range(n):
            if p >= 0:
                mat[i][i+p] = v[i]
            else:
                mat[i - p][i] = v[i]

        return Matrix(mat)
    
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

    def perm2pat(p):
        n = len(p)
        p = np.zeros((n,n))
        for i in range(n):
            P[i,p[i] - 1] = 1
        return P

    def frob(A):
        total = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                total += A[i][j] **2
        return math.sqrt(total)

    def Transpose(A):
        return Matrix([[A.data[j][i] for j in range(A.rows)] for i in range(A.columns)])


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

    
    def solve(A,b):
        L,U,P, _ = lu(A)

        Pb = [sum(P[i][j] * b[j] for j in range(len(b))) for i in range(len(b))]
        y = forwsub(L,Pb)
        x = backsub(U,y)
        x = x[::-1]
        Ax = [sum(A[i][j] * x[::-1][j] for j in range(len(x))) for i in range(len(A))]
        error = math.sqrt(sum((Ax[i] - b[i])**2 for i in range(len(b))))

        return x, error
    

    def det(A):
        if len(A.data) != len(A.data[0]):
            raise ValueError("Function is only defined for ssquare matricies")

        _,U = getLU(A.data)
        product = 1
        for i in range(len(U.data)):
            product *= U.data[i][i]
        return product

    def mat2perm(p):

        perm = []
        for row in p:
            perm.append(row.index(1))
        return perm

    def sgn(p):

        cnt = 0 
        n = len(p)
        for i in range(n):
            for j in range(i + 1,n):
                if p[i] > p[j]:
                    inversion += 1
        return -1 if cnt % 2 else 1
