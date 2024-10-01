import matplotlib.pyplot as plt
import numpy as np

i_st, fSu_st, qout = np.loadtxt('starve.txt', unpack=True)
i_ng, fSu_ng, qin = np.loadtxt('drought.txt', unpack=True)

fig, ax1 = plt.subplots()

ax1.set_ylim(0,20)
ax1.plot(i_st,1000*qout,'g--')
ax1.plot(i_ng,1000*qin,'r-.')
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Flux (g[Su] m$^{-2}$ d$^{-1}$)')
plt.text(750,2,'No growth',color='red')
plt.text(400,0.5,'Starvation',color='green')
plt.text(100,12,'$q_{in}$',color='red')
plt.text(100, 2,'$q_{out}$',color='green')
ax1.plot(i_ng[0:499],1000*qout[0:499],'g-')
ax1.plot(i_ng[0:499],1000*qin[0:499],'r-')

ax2 = ax1.twinx()

ax2.plot(i_st,fSu_st,'b--')
ax2.plot(i_ng,fSu_ng,'b-.')
ax2.plot(i_ng[0:499],fSu_ng[0:499],'b-')
ax2.set_ylabel('Sucrose concentration (fraction of DM)')

plt.text(1000,0.06,'No growth',color='blue')
plt.text(1500,0.011,'Starvation',color='blue')
plt.text(300,0.031,'[$Su$]',color='blue')

# For vectorized output.
plt.savefig('Figure_4.pdf')

plt.show()
