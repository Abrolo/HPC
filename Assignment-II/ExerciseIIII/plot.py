import numpy as np
import matplotlib.pyplot as plt

datadir    = ''
flops = input("Flops y or n?: ")
if(flops=="y"):
    dataname_l = 'list_flop.txt'
    dataname_a = 'array_flop.txt'
    dataname_n = 'numpy_flop.txt'
else:
    dataname_l = 'list.txt'
    dataname_a = 'array.txt'
    dataname_n = 'numpy.txt'
    
time_l     = np.loadtxt(dataname_l)
time_a     = np.loadtxt(dataname_a)
time_n     = np.loadtxt(dataname_n)
# all for all curves in one figure
plot_type = input("Enter plot type: ")

plt.figure(figsize=(8.5, 6))
if(flops=="y"):
    if(plot_type=="all"):
        plt.plot(time_l[:,0],time_l[:,1],'-.',color='black')
        plt.plot(time_a[:,0],time_a[:,1],'-.',color='green')
        plt.plot(time_n[:,0],time_n[:,1],'-.',color='blue')
        plt.legend(('list','Array','NUmpy'),
                   loc='best', prop={'size': 15})
        plt.xlabel(r"$n$",fontsize=18)
        plt.ylabel(r"$FLPO/s$",fontsize=18)
        plt.xlim(xmin=0)
        plt.ylim(ymin=0)
        plt.savefig('flops_all.png')
        #plt.show() 
    else:
        plt.plot(time_l[:,0],time_l[:,1],'-.',color='black')
        plt.plot(time_a[:,0],time_a[:,1],'-.',color='green')
        plt.legend(('List','Array'),loc='best', prop={'size': 15})
        plt.xlabel(r"$n$",fontsize=18)
        plt.ylabel(r"$FLPO/s$",fontsize=18)
        plt.xlim(xmin=0)
        plt.ylim(ymin=0)
        plot_type = "flops_"+plot_type
        plt.savefig(plot_type+".png")
        #plt.show()
else:
    if(plot_type=="all"):
        plt.plot(time_l[:,0],time_l[:,1],'-.',color='black')
        plt.plot(time_a[:,0],time_a[:,1],'-.',color='green')
        plt.plot(time_n[:,0],time_n[:,1],'-.',color='blue')
        plt.legend(('list','Array','Numpy'),
                   loc='best', prop={'size': 15})
        plt.xlabel(r"$n * n$",fontsize=18)
        plt.ylabel(r"Run time",fontsize=18)
        plt.xlim(xmin=0)
        plt.ylim(ymin=0)
        plt.savefig('all.png')
        #plt.show() 
    elif(plot_type=="numpy"):
        plt.plot(time_n[:,0],time_n[:,1],'-.',color='blue')
        plt.legend(('Numpy'),loc='best', prop={'size': 15})
        plt.xlabel(r"$n * n$",fontsize=18)
        plt.ylabel(r"Run time",fontsize=18)
        plt.xlim(xmin=0)
        plt.ylim(ymin=0)
        plt.savefig(plot_type+".png")
        #plt.show()
