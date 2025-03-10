import numpy as np
import matplotlib.pyplot as plt
import sys
import timeit
                
t0 = timeit.time.time()

def rnbhsigma(q):
   return (1./np.sqrt(2.) ) * (9.-4.*q**2+3.*np.sqrt(9.-8.*q**2))/np.sqrt(3.-2.*q**2+np.sqrt(9.-8.*q**2))
   

fig = plt.figure()
fontsize1 = 15
fontsize2 = 14
fontsize3 = 13


sigma1, delta1 =5.8, 1.4
sigma2, delta2 =5.16, 0.43
labelnumset = [1]

for i in range(len(labelnumset)):   
   datash = np.genfromtxt('bumblebeebh_data.txt')
   datash0, datash1, datash2 = datash[:,0], datash[:,1], datash[:,3] 
   plt.plot( datash0,  datash2 )

   

xset = np.arange(0, 1, 0.0001)
xsetlong = np.arange(0, 10, 0.0001)
#plt.plot(xset, rnbhsigma(xset), linestyle='--', label=r'$\xi=0$ (RN metric)' ) 
plt.fill_between(xsetlong, sigma1+delta1, sigma1-delta1, alpha=0.3)
plt.fill_between(xsetlong, sigma2+delta2, sigma2-delta2, alpha=0.3 )



plt.xlim(datash0[0], datash0[-1])
plt.ylim(0, 7.5)
plt.ylabel(r'$\sigma_{\rm lr} [M]$', fontsize=fontsize1)
plt.xlabel(r'$|Q| [M]$', fontsize=fontsize1)
plt.xticks(fontsize=fontsize2)
plt.yticks(fontsize=fontsize2)
#plt.legend(loc='lower right', fontsize=fontsize3, frameon=False)


plt.savefig("bumblebeebh_plot.pdf", format='pdf', bbox_inches="tight")
print( '\n *** uses %.2f seconds\n' % (timeit.time.time() - t0))
#plt.show ()
