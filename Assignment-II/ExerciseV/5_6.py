import math
import numpy as np
import random

from timeit import default_timer as timer
import matplotlib.pyplot as plt
def fill_w(N):
    W = [[0 for k in range(N)] for n in range(N)]
    w = math.e**(-1j*2*math.pi/N)
    for row in range(N):
        for col in range(N):
            W[row][col] = w**((row)*(col))
            #W[row][col] = W[row][col]/math.sqrt(N)
    return W

def vector_matrix_mul(x, W, N):
    Xo = [0 for i in range(N)]
    for row in range(N):
        for col in range(N):
            Xo[row] += W[row][col]*x[col]
    return Xo

def fast_dft(N):
    w = np.exp(-1j * 2 * np.pi / N)
    J,K = np.meshgrid(np.arange(N), np.arange(N))
    DFT = np.power(w,J*K)

    return DFT

def iterate_using_library():
    N = 8
    timeList = []
    while(N<=1024):
        t1 = timer()
        x = np.zeros(N)
        for i in range(N):
            x[i]= random.randint(1,10)

        np.fft.fftn(x)
        t2 = timer()

        timeList.append(t2-t1)
        N *= 2
    
    return timeList

def iterate_using_optimization():
    N = 8
    timeList = []
    while(N<=1024):
        t1 = timer()
        x = np.zeros(N)
        for i in range(N):
            x[i]= random.randint(1,10)

        W_fast = fast_dft(N)
        res = np.dot(W_fast, x)
        
        t2 = timer()
        timeList.append(t2-t1)
        
        N *= 2
    
    return timeList

def iterate_naive():
    N = 8
    timeList = []
    while(N<=1024):
        t1 = timer()
        x = np.zeros(N)
        for i in range(N):
            x[i]= random.randint(1,10)

        W_slow = fill_w(N)
        res = vector_matrix_mul(x, W_slow, N)
        
        t2 = timer()
        timeList.append(t2-t1)
        
        N *= 2
    
    return timeList

timeLib = iterate_using_library()
timeOpt = iterate_using_optimization()
timeNaive = iterate_naive()
plt.ylabel("Execution time (seconds)")
plt.xlabel("Input size")
plt.title("Different execution time for varying input size")
plt.plot([8,16,32,64,128,256,512,1024], (timeLib), label = "Library DFT")
plt.plot([8,16,32,64,128,256,512,1024], (timeOpt), label = "Optimized DFT")
plt.plot([8,16,32,64,128,256,512,1024], (timeNaive), label = "Naive DFT")
plt.legend()
plt.show()
