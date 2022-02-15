import math
import numpy as np
import random
import pytest
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def fill_w(N):
    W = [[0 for k in range(N)] for n in range(N)]
    for i in range(N):
        W[0][i] = 1
        W[i][0] = 1
    for row in range(1,N):
        for col in range(1,N):
            W[row][col] = (math.e**(-1j * 2 * math.pi/N))**(row*col)
            W[row][col] = W[row][col]/math.sqrt(N)
    return W

def vector_matrix_mul(x, W, N):
    Xo = [0 for i in range(N)]
    for row in range(N):
        for col in range(N):
            Xo[row] += W[row][col]*x[row]
    return Xo

def test_vector_matrix_mul(x, W, N):
    assert vector_matrix_mul(x, W, N)


N = 3
x = []
for i in range(N):
    x.append(random.randint(0,10))

print(x)
W = fill_w(N)
print(W)
Xo = vector_matrix_mul(x, W, N)
print(Xo)