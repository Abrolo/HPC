import numpy as np

def copy_list(a,c, n):
    for j in range(n):
        c[j] = a[j]
def copy_numpy(a,c):
    np.copyto(c,a)
# scale 
def scale_list(b,c,scalar,n):
    for j in range(n):
        b[j] = scalar*c[j]
def scale_numpy(b,c,scalar):
    b = scalar*c
#sum
def sum_list(a,b,c,n):
    for j in range(n):
        c[j] = a[j]+b[j]
def sum_numpy(a,b,c):
    c = a+b
        
# triad       
def triad_list(a,b,c,scalar, n):
    for j in range(n):
        a[j] = b[j]+scalar*c[j]

def triad_numpy(a,b,c,scalar):
    c = scalar*c
    a = b+c