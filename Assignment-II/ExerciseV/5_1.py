import math
import numpy as np
import random
import pytest
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

def test_vector_matrix_mul():
    N = 256
    x = np.zeros(N)
    for i in range(N):
        x[i]= random.randint(1,10)
        
    W_slow = fill_w(N)
    W_fast = fast_dft(N)

    actual = vector_matrix_mul(x, W_slow, N)
    expected= np.dot(W_fast, x)
    #Converting to np array just to be sure
    actual = np.array(actual)

    for i in range(N):
        assert round(np.real(actual[i]),2) == round(np.real(expected[i]),2)
        assert round(np.imag(actual[i]),2) == round(np.imag(expected[i]),2)
