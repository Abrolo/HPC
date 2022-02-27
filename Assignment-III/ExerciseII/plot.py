import numpy as np
import matplotlib.pyplot as plt

datadir    = ''
plt.figure(figsize=(8.5, 6))
Cython_optimize = input("Use Cython optimizion; Enter y or n: ")
if(Cython_optimize=="y"):
    array_type   = input("Enter the array type: ")
    dataname     = array_type+".txt"
    dataname_op  = array_type+"_op.txt"
    time         = np.loadtxt(dataname)
    time_op      = np.loadtxt(dataname_op)
    plt.plot(time[:,0],time[:,1],'-.',color='blue')
    plt.plot(time_op[:,0],time_op[:,1],'-.',color='green')
    plt.legend((array_type,array_type+" with Cython optimization"),
	       loc='best', prop={'size': 15})
    plt.xlabel(r"$n$",fontsize=18)
    plt.ylabel(r"$Run time$",fontsize=18)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    #plt.savefig("compare_op_"+array_type+".png")
    plt.show()
    
else:
    dataname_l  = 'list.txt'
    dataname_a  = 'array.txt'
    dataname_n  = 'numpy.txt'
    dataname_nv = 'numpyvector.txt'
    time_l  = np.loadtxt(dataname_l)
    time_a  = np.loadtxt(dataname_a)
    time_n  = np.loadtxt(dataname_n)
    time_nv = np.loadtxt(dataname_nv)
    plt.plot(time_l[:,0],time_l[:,1],'-.',color='black')
    plt.plot(time_a[:,0],time_a[:,1],'-.',color='green')
    plt.plot(time_n[:,0],time_n[:,1],'-.',color='red')
    plt.plot(time_nv[:,0],time_nv[:,1],'-.',color='blue')
    plt.legend(('list','Array','Numpy using loop','Numpy using vector operation'),
               loc='best', prop={'size': 15})
    plt.xlabel(r"$n$",fontsize=18)
    plt.ylabel(r"$Run time$",fontsize=18)
    plt.xlim(xmin=0)
    plt.ylim(ymin=0)
    plt.savefig('AllArrays.png')
    #plt.show() 

