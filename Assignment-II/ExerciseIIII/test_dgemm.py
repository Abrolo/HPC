import numpy as np
from array import array
import pytest

def initialize(a,b,c,n):
    for i in range(n):
        for j in range(n):
            a[i][j] = j + n*i
            b[i][j] = 3.14*(j + n*i)
            c[i][j] = 0.0
    return (a,b,c)
def dgemm_numpy(a,b,c,n):
    return (np.matmul(a,b)+c)

def dgemm_list(a,b,c,n):
    for i in range(n): 
        for j in range(n):
            for k in range(n):
                c[i][j] = a[i][k]*b[k][j] + c[i][j]
    return c
# set the same array size used in blas_example.c run
n = 6 

datadir    = ''
dataname = 'reference.txt'
reference    = np.loadtxt(dataname)
# list type
a_l = [[0 for x in range(n)] for x in range(n)]
b_l= [[0 for x in range(n)] for x in range(n)]
c_l = [[0 for x in range(n)] for x in range(n)]
(a_l,b_l,c_l) = initialize(a_l,b_l,c_l,n)
c_l = dgemm_list(a_l,b_l,c_l,n)

# array type
a_a = [array('f', (0 for x in range(n))) for x in range(n)]
b_a = [array('f', (0 for x in range(n))) for x in range(n)]
c_a = [array('f', (0 for x in range(n))) for x in range(n)]
(a_a,b_a,c_a) = initialize(a_a,b_a,c_a,n)
c_a = np.round(dgemm_list(a_a,b_a,c_a,n),2)

#numpy type
a_n = np.zeros(shape=(n,n))
b_n = np.zeros(shape=(n,n))
c_n = np.zeros(shape=(n,n))
initialize(a_n,b_n,c_n,n)
c_n = dgemm_numpy(a_n,b_n,c_n,n)

@pytest.mark.parametrize(
    "test_input,reference",
    [(c_a, reference),(c_a, reference),(c_n, reference)],
)

def test_result(test_input,reference):
    np.testing.assert_allclose(test_input,reference)
