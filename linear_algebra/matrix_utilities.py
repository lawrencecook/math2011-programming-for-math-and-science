from collections import UserList

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
        import numpy as np
        inv = np.linalg.inv(np.array(self.data))
        return Matrix(inv.tolist())

#Example 9.5
A = Matrix([[1,-1,1],[2,-1,0],[1,-2,2]])
B = Matrix([[2,0,-1],[4,-1,-2],[3,-1,-1]])
print(A*B)
print(B*A)
print("Since A*B and B*A gives the Identity Matrix, we can see their Inverses of each other")

#Problem 2
A = Matrix([[1,2],[3,4]])
B = Matrix([[2,1],[4,3]])
C = Matrix([[1,2,1],[0,1,2]])
D = Matrix([[3,1],[1,-5],[2,3]])
x = Vector([2,1])
y = Vector([0.5,-1,0])

#a-i
print(A*x)
print((A+B)*x)
print(C*y)
try:
    print(D*y)
except ValueError as e:
    print("D * y raised an error(as expected):",e)
print(D*x)
print(B*A)
print(A*C)
print(C*D)
print(D*C)

#9 - Adding different functions
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

def diag(A):
    if type(A) != Matrix:
        raise TypeError("Input must be Matrix")
    return Vector([A[i][i] for i in range(min(len(A), len(A[0])))])
