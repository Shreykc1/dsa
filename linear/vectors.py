import math

def userinput():
    rows = int(input("Enter no of rows: "))
    matrix = [0 for i in range(rows)]
    
    for i in range(rows):
        matrix[i] = int(input(f"Enter number {i+1}: "))
    print()
    return matrix

def add(m1,m2):
    return [m1[i] + m2[i] for i in range(len(m1))]

def subtract(m1,m2):
    return [m1[i] - m2[i] for i in range(len(m1))]

def dot(m1,m2):
    result = 0
    
    for i in range(len(m1)):
        result += (m1[i]*m2[i])
        
    return result


def minor(m,row,col):
    temp = []
    
    for i in range(3):
        if i == row:
            continue
        for j in range(3):
            if j == col:
                continue
            temp.append(m[i][j])
    return ((temp[0] * temp[3]) - (temp[1] * temp[2]))

def determinant(m):
    return [minor(m, 0, 0), minor(m, 0, 1), minor(m, 0, 2)]


def cross(m1,m2):
        

    result = [[1,1,1]]
    result.append(m1)
    result.append(m2)
    
    return determinant(result)


def magnum(m):
    s = 0
    
    for i in m:
        s += (i**2)   
    return math.sqrt(s)

def angle(m1,m2):
    
    u = magnum(m1)
    v = magnum(m2)
   
    cos_theta = dot(m1,m2)/(u*v)
    theta=math.acos(cos_theta)
    return theta*(180/math.pi)


def projection(u,v):
    dot = dot(u,v)
    mag = magnum(v)**2
    
    result = dot/mag
    return [a*result for a in v]
    
def distance(m1,m2):
    result = 0
    for i in range(len(m1)):
        result += (m1[i]-m2[i])**2
    return math.sqrt(result)    








m1 = userinput()
m2 = userinput()

m3 = angle(m1,m2)
print(m3)