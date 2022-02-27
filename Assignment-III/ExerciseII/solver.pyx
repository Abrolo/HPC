from numpy import roll
import numpy as np
cimport numpy as np

def gauss_seidel(f,nx,ny):
    cdef unsigned int i, j
    newf = f.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            newf[i][j] = 0.25 * (newf[i][j+1]+newf[i][j-1]+newf[i+1][j]+newf[i-1][j])
    return newf

def gauss_seidel_np(f,nx,ny):
    cdef unsigned int i, j
    cdef double[:,:] newf = np.empty((nx,ny),dtype=np.double)
    newf = f.copy()
    
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            newf[i,j] = 0.25 * (newf[i,j+1]+newf[i,j-1]+newf[i+1,j]+newf[i-1,j])
    return newf
    
def gauss_numpy(f):
    return (0.25*(roll(f,+1,0)+roll(f,-1,0)+roll(f,+1,1)+roll(f,-1,1)))

def initialize(x,nx,ny):
    cdef unsigned int i, j, xb, yb
    xb = nx-1
    yb = ny-1
    for i in range(nx):
        x[i][0] = 0.
        x[i][yb] = 0.
    for j in range(ny):
        x[0][j] = 0.
        x[xb][j] = 0.
    return x

def initialize_np(x,nx,ny):
    cdef unsigned int i, j, xb, yb
    cdef double[:,:] xn = np.empty((nx,ny),dtype=np.double)
    xn = x.copy()
    xb = nx-1
    yb = ny-1
    for i in range(nx):
        xn[i][0] = 0.
        xn[i][yb] = 0.
    for j in range(ny):
        xn[0][j] = 0.
        xn[xb][j] = 0.
    return xn