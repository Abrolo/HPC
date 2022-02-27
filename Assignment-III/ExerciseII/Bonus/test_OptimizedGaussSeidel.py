import numpy as np
import random
from cffi import FFI
from timeit import default_timer as timer
import pytest

def initialize(x,nx,ny):
    for i in range(nx):
        x[i][0] = 0.
        x[i][ny-1] = 0.
    for j in range(ny):
        x[0][j] = 0.
        x[nx-1][j] = 0.
    return x

def gauss_seidel(f,nx,ny):
    newf = f.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            newf[i][j] = 0.25 * (newf[i][j+1]+newf[i][j-1]+newf[i+1][j]+newf[i-1][j])
    return newf

n = int(input("Enter the initial array size: "))
iteration = int(input("Enter the number of iteration for the Gauss-Seidel solver: "))

x = np.random.rand(n,n)
nx,ny = x.shape
x = initialize(x,nx,ny)
times = timer()
for i in range(iteration):
    x = gauss_seidel(x,nx,ny)
times = timer() - times
print("Execution time Python: ",times)

x_o = np.random.rand(n,n)
nx,ny = x_o.shape
x_o = initialize(x,nx,ny)
ffi = FFI()
lib = ffi.dlopen('./Gauss_seidel.so')
ffi.cdef("void gauss_seidel(double *, int);")
xptr = ffi.cast("double *", ffi.from_buffer(x))
times = timer()
for i in range(iteration):
    lib.gauss_seidel(xptr, n)
times = timer() - times
print("Execution time optimized Python: ",times)

@pytest.mark.parametrize(
    "test_input,reference",
    [(x_o, x)],
)

def test_result(test_input,reference):
    np.testing.assert_allclose(test_input,reference)
