import numpy as np
from timeit import default_timer as timer
from matplotlib import rc
import matplotlib.pyplot as plt
import numexpr as ne

def initialize(a,b,c,n):
    for i in range(n):
        for j in range(n):
            a[i][j] = j + n*i
            b[i][j] = 3.14*(j + n*i)
            c[i][j] = 0.0
    return (a,b,c)
def dgemm_numpy(a,b,c,n):
    return (np.matmul(a,b)+c)

def dgemm_numexpr(a,b,c,n):
    ne.evaluate("a*b+c",out=c)

n = int(input("Enter the array initial array size (please enter 2): "))
iteration = int(input("Enter the number of iteration (for final result, please enter 250): "))
optimization = input("Enter y or n for using numexpr: ")
times = np.zeros(shape=(iteration,2))

if(optimization=="y"):
    for k in range(iteration):
        a = np.zeros(shape=(n,n))
        b = np.zeros(shape=(n,n))
        c = np.zeros(shape=(n,n))
        initialize(a,b,c,n)
    times[k][1] = timer()
    dgemm_numexpr(a,b,c,n)
    times[k][1] = timer() - times[k][1]
    times[k][0] = n
    n +=2
    array_type = "Numexpr_opt"
elif(optimization=="n"):
    for k in range(iteration):
        a = np.zeros(shape=(n,n))
        b = np.zeros(shape=(n,n))
        c = np.zeros(shape=(n,n))
        initialize(a,b,c,n)
        times[k][1] = timer()
        c = dgemm_numpy(a,b,c,n)
        times[k][1] = timer() - times[k][1]
        times[k][0] = n
        n +=2
    array_type = "Numpy_opt"

f = open(array_type+".txt", "w")
for i in times:
    f.write(f"{i[0]}\t{i[1]}\n")
f.close()
