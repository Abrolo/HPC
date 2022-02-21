import numpy as np
from array import array
from matplotlib import rc
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import sys

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
iteration = int(input("Enter the number of iteration: "))
times = np.zeros(shape=(iteration,2))
flop = input("Enter y or n for FLOP: ")
# write : w ; p : plot
output = input("Enter w or p: ")

if(array_type=="list"):
    for k in range(iteration):
        a = [[0 for x in range(n)] for x in range(n)]
        b = [[0 for x in range(n)] for x in range(n)]
        c = [[0 for x in range(n)] for x in range(n)]
        initialize(a,b,c,n)
        times[k][1] = timer()
        dgemm_list(a,b,c,n)
        times[k][1] = timer() - times[k][1]
        if(flop=="y"):
            times[k][0] = n
            times[k][1] = (n*n*n)/times[k][1]
        elif(flop=="n"):
            times[k][0] = n*n
        n +=2
elif(array_type=="array"):
    for k in range(iteration):
        a = [array('f', (0 for x in range(n))) for x in range(n)]
        b = [array('f', (0 for x in range(n))) for x in range(n)]
        c = [array('f', (0 for x in range(n))) for x in range(n)]
        initialize(a,b,c,n)
        times[k][1] = timer()
        dgemm_list(a,b,c,n)
        times[k][1] = timer() - times[k][1]
        if(flop=="y"):
            times[k][0] = n
            times[k][1] = (n*n*n)/times[k][1]
        elif(flop=="n"):
            times[k][0] = n*n
        c = np.round(c,2)
        n +=2
elif(array_type=="numpy"):
    for k in range(iteration):
        a = np.zeros(shape=(n,n))
        b = np.zeros(shape=(n,n))
        c = np.zeros(shape=(n,n))
        initialize(a,b,c,n)
        times[k][1] = timer()
        c = dgemm_numpy(a,b,c,n)
        times[k][1] = timer() - times[k][1]
        if(flop=="y"):
            times[k][0] = n
            times[k][1] = (n*n*n)/times[k][1]
        elif(flop=="n"):
            if(output=="p"):
                times[k][0] = sys.getsizeof(a)
                times[k][0] +=sys.getsizeof(b)
                times[k][0] +=sys.getsizeof(c)
            elif(output=="w"):
                times[k][0] = n*n
        n +=2

if(output=="p" and array_type=="numpy"):
    plt.figure(figsize=(8.5, 6))
    plt.plot(times[:,0],times[:,1],'-.',color='blue')
    plt.legend(('Numpy'),loc='best', prop={'size': 15})
    plt.xlabel(r"Memory usag",fontsize=18)
    plt.ylabel(r"Run time",fontsize=18)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    #plt.savefig(plot_type+".png")
    plt.show()
elif(output=="w"):
    if(flop=="y"):
        array_type+="_flop"
    f = open(array_type+".txt", "w") 
    for i in times:
        f.write(f"{i[0]}\t{i[1]}\n")
    f.close()
