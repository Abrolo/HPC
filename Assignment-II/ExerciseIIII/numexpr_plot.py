import numpy as np
import matplotlib.pyplot as plt
datadir    = ''

dataname_ex = 'Numexpr_opt.txt'
dataname_np = 'Numpy_opt.txt'

time_np     = np.loadtxt(dataname_np)
time_ex     = np.loadtxt(dataname_ex)

plt.figure(figsize=(8.5, 6))
plt.plot(time_np[:,0],time_np[:,1],'-.',color='black')
plt.plot(time_ex[:,0],time_ex[:,1],'-.',color='green')
plt.legend(('Numpy','Numexpr'),loc='best', prop={'size': 15})
plt.xlabel(r"$n$",fontsize=18)
plt.ylabel(r"$Run time$",fontsize=18)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plot_type = "Compare_numpy_numexpr"
plt.savefig(plot_type+".png")
#plt.show()
