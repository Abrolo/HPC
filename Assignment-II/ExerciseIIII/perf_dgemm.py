import numpy as np
from array import array

def initialize(a,b,c,n):
    for i in range(n):
        for j in range(n):
            a[i][j] = j + n*i
            b[i][j] = 3.14*(j + n*i)
            c[i][j] = 0.0
            
def dgemm_numpy(a,b,c,n):
    return (np.matmul(a,b)+c)

def dgemm_list(a,b,c,n):
    for i in range(n): 
        for j in range(n):
            for k in range(n):
                c[i][j] = a[i][k]*b[k][j] + c[i][j]

array_type = input("Enter the array type: ")
n = int(input("Enter the array size: "))

if(array_type=="list"):
    a = [[0 for x in range(n)] for x in range(n)]
    b = [[0 for x in range(n)] for x in range(n)]
    c = [[0 for x in range(n)] for x in range(n)]
    initialize(a,b,c,n)
    dgemm_list(a,b,c,n)
elif(array_type=="array"):
    a = [array('d', (0 for x in range(n))) for x in range(n)]
    b = [array('d', (0 for x in range(n))) for x in range(n)]
    c = [array('d', (0 for x in range(n))) for x in range(n)]
    initialize(a,b,c,n)
    dgemm_list(a,b,c,n)
elif(array_type=="numpy"):
    a = np.zeros(shape=(n,n))
    b = np.zeros(shape=(n,n))
    c = np.zeros(shape=(n,n))
    initialize(a,b,c,n)
    c = dgemm_numpy(a,b,c,n)
    
#f = open(array_type+".txt", "w") 
#for i in times:
#    f.write(f"{i[0]}\t{i[1]}\n")
#f.close()
