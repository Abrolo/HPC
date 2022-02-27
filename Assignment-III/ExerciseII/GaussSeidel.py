import numpy as np
from numpy import roll
from array import array
import random
from timeit import default_timer as timer
import solver

def initialize(x,nx,ny):
    for i in range(nx):
        x[i][0] = 0.
        x[i][ny-1] = 0.
    for j in range(ny):
        x[0][j] = 0.
        x[nx-1][j] = 0.
    return x
def gauss_numpy(f):
    return (0.25*(roll(f,+1,0)+roll(f,-1,0)+roll(f,+1,1)+roll(f,-1,1)))    

def gauss_seidel(f,nx,ny):
    newf = f.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            newf[i][j] = 0.25 * (newf[i][j+1]+newf[i][j-1]+newf[i+1][j]+newf[i-1][j])
    return newf

array_type = input("Enter the array type: ")
n = int(input("Enter the initial array size: "))
iteration = int(input("Enter the number of iteration for the Gauss-Seidel solver: "))
refinement = int(input("Enter the number of refinement: "))
Cython_optimize = input("Use Cython optimizion; Enter y or n: ") 
times = np.zeros(shape=(refinement,2))

if(array_type=="list"):
    for k in range(refinement):
        x = [[random.random() for x in range(n)] for x in range(n)]
        nx,ny = np.asarray(x).shape
        if(Cython_optimize=="y"):
            times[k][1] = timer()
            x = solver.initialize(x,nx,ny)
            for i in range(iteration):
                x = solver.gauss_seidel(x,nx,ny)
            times[k][1] = timer() - times[k][1]
        else:
            times[k][1] = timer()
            x = initialize(x,nx,ny)
            for i in range(iteration):
                x = gauss_seidel(x,nx,ny)
            times[k][1] = timer() - times[k][1]
        times[k][0] = n
        n*=2
elif(array_type=="array"):
    for k in range(refinement):
        x = [array('d', (random.random() for x in range(n))) for x in range(n)]
        nx,ny = np.asarray(x).shape
        if(Cython_optimize=="y"):
            times[k][1] = timer()
            x = solver.initialize(x,nx,ny)
            for i in range(iteration):
                x = solver.gauss_seidel(x,nx,ny)
            times[k][1] = timer() - times[k][1]
        else:
            times[k][1] = timer()
            x = initialize(x,nx,ny)
            for i in range(iteration):
                x = gauss_seidel(x,nx,ny)
            times[k][1] = timer() - times[k][1]
        times[k][0] = n
        n*=2
elif(array_type=="numpy"):
    for k in range(refinement):
        x = np.random.rand(n,n)
        nx,ny = x.shape
        if(Cython_optimize=="y"):
            times[k][1] = timer()
            x = solver.initialize_np(x,nx,ny)
            for i in range(iteration):
                x= solver.gauss_seidel_np(x,nx,ny)
            times[k][1] = timer() - times[k][1]
        else:
            times[k][1] = timer()
            x = initialize(x,nx,ny)
            for i in range(iteration):
                x = gauss_seidel(x,nx,ny)
            times[k][1] = timer() - times[k][1]
        times[k][0] = n
        n*=2
elif(array_type=="numpyvector"):
    for k in range(refinement):
        x = np.random.rand(n,n)
        nx,ny = x.shape
        if(Cython_optimize=="y"):
            times[k][1] = timer()
            x = solver.initialize_np(x,nx,ny)
            for i in range(iteration):
                x= solver.gauss_numpy(x)
            times[k][1] = timer() - times[k][1]
        else:
            times[k][1] = timer()
            x = initialize(x,nx,ny)
            for i in range(iteration):
                x = gauss_numpy(x)
            times[k][1] = timer() - times[k][1]
        times[k][0] = n
        n*=2

if(Cython_optimize=="y"):
    array_type+="_op"
f = open(array_type+".txt", "w")
for i in times:
    f.write(f"{i[0]}\t{i[1]}\n")
f.close()
