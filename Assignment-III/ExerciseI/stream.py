import numpy as np
from array import array
from timeit import default_timer as timer
import matplotlib.pyplot as plt
import cythonfn as cfn

### STREAM Benchmark for list ###
# copy

def initialize_list(a,b,c):
    for j in range(STREAM_ARRAY_SIZE):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = 0.0
def initialize_numpy(a,b,c):
    a = 1.0
    b = 2.0
    c = 0.0
    
STREAM_ARRAY_SIZE = int(input("Enter the initial vector size: "))
scalar = 2.0
type_arry = input("Enter the array type: ")
iteration = int(input("Enter the number of iteration: "))
times = np.zeros(shape=(iteration,4))
array_size = np.zeros(iteration)
plt.figure(figsize=(8.5, 6))
if(type_arry=="list"):
    for k in range(iteration):
        n = STREAM_ARRAY_SIZE
        array_size[k] = STREAM_ARRAY_SIZE
        a = list(range(STREAM_ARRAY_SIZE))
        b = list(range(STREAM_ARRAY_SIZE))
        c = list(range(STREAM_ARRAY_SIZE))
        initialize_list(a,b,c)

        times[k][0] = timer()
        cfn.copy_list(a,c, n)
        times[k][0] = timer() - times[k][0]

        times[k][1] = timer()
        cfn.scale_list(b,c,scalar, n)
        times[k][1] = timer() - times[k][1]

        times[k][2] = timer()
        cfn.sum_list(a,b,c, n)
        times[k][2] = timer() - times[k][2]

        times[k][3] = timer()
        cfn.triad_list(a,b,c,scalar,n )
        times[k][3] = timer() - times[k][3]   

        STREAM_ARRAY_SIZE *=2

    first_data = "List : copy"
    second_data = "List : scale"
    third_data = "List : sum"
    fourth_data = "List : triad"
    plot_name = "List_cython.png"
    if(iteration==1):
        print(first_data,str(times[k][0])+" s",sep="         ")
        print(second_data,str(times[k][1])+" s",sep="         ")
        print(third_data,str(times[k][2])+" s",sep="         ")
        print(fourth_data,str(times[k][3])+" s",sep="         ")
        
elif(type_arry=="array"):
    for k in range(iteration):
        n = STREAM_ARRAY_SIZE
        array_size[k] = STREAM_ARRAY_SIZE
        a = array('f',range(STREAM_ARRAY_SIZE))
        b = array('f',range(STREAM_ARRAY_SIZE))
        c = array('f',range(STREAM_ARRAY_SIZE))
        initialize_list(a,b,c)
        times[k][0] = timer()
        cfn.copy_list(a,c, n)
        times[k][0] = timer() - times[k][0]
        times[k][1] = timer()
        cfn.scale_list(b,c,scalar,n)
        times[k][1] = timer() - times[k][1]
        times[k][2] = timer()
        cfn.sum_list(a,b,c,n)
        times[k][2] = timer() - times[k][2]
        times[k][3] = timer()
        cfn.triad_list(a,b,c,scalar,n)
        times[k][3] = timer() - times[k][3]
        STREAM_ARRAY_SIZE *=2
        
    first_data = "Array : copy"
    second_data = "Array : scale"
    third_data = "Array : sum"
    fourth_data = "Array : triad"
    plot_name =	"Array_cython.png"
    if(iteration==1):
        print(first_data,str(times[k][0])+" s",sep="         ")
        print(second_data,str(times[k][1])+" s",sep="         ")
        print(third_data,str(times[k][2])+" s",sep="         ")
        print(fourth_data,str(times[k][3])+" s",sep="         ")
        
elif(type_arry=="numpy"):
    for k in range(iteration):
        n = STREAM_ARRAY_SIZE
        array_size[k] = STREAM_ARRAY_SIZE
        a = np.arange(STREAM_ARRAY_SIZE)
        b = np.arange(STREAM_ARRAY_SIZE)
        c = np.arange(STREAM_ARRAY_SIZE)
        initialize_numpy(a,b,c)
        times[k][0] = timer()
        cfn.copy_numpy(a,c)
        times[k][0] = timer() - times[k][0]
        times[k][1] = timer()
        cfn.scale_numpy(b,c,scalar)
        times[k][1] = timer() - times[k][1]
        times[k][2] = timer()
        cfn.sum_numpy(a,b,c)
        times[k][2] = timer() - times[k][2]
        times[k][3] = timer()
        cfn.triad_numpy(a,b,c,scalar)
        times[k][3] = timer() - times[k][3]
        STREAM_ARRAY_SIZE *=2
        
    first_data = "Numpy : copy"
    second_data = "Numpy : scale"
    third_data = "Numpy : sum"
    fourth_data = "Numpy : triad"
    plot_name =	"Numpy_cython.png"
    if(iteration==1):
        print(first_data,str(times[k][0])+" s",sep="         ")
        print(second_data,str(times[k][1])+" s",sep="         ")
        print(third_data,str(times[k][2])+" s",sep="         ")
        print(fourth_data,str(times[k][3])+" s",sep="         ")
        
if(iteration!=1):
    plt.plot(array_size[:],times[:,0],'-.',color='black')
    plt.plot(array_size[:],times[:,1],'-.',color='red')
    plt.plot(array_size[:],times[:,2],'-.',color='blue')
    plt.plot(array_size[:],times[:,3],'-.',color='green')
    plt.title("STREAM benchmarks using Cython")
    plt.legend((first_data, second_data, third_data, fourth_data),
               loc='best', prop={'size': 15})
    plt.xlabel(r"Vector length",fontsize=18) 
    plt.ylabel(r"Run time",fontsize=18)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.savefig(plot_name)
