# load package
import matplotlib as mpl
import matplotlib.pyplot as plt
#import matplotlib.font_manager
from matplotlib.ticker import MultipleLocator,FormatStrFormatter,MaxNLocator
import numpy as np
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

#mpl.rcParams['pdf.fonttype'] = 42
#mpl.rcParams['ps.fonttype'] = 42
#mpl.rcParams['font.family'] = 'Arial'

j, alpha, qout, qoutp, fSu, fi, fa, dGda, dGdap = np.loadtxt('a.txt', unpack=True)
jb, betab, qoutb, qoutpb, fSub, fib, fab, dGdbb, dGdbpb = np.loadtxt('b.txt', unpack=True)

fig = plt.figure(figsize=(7.5,6))

x1 = 0.1
y1 = 0.11
xsp = 0.5
ysp = 0.5
xsize = 0.35
ysize = 0.35

ax = plt.axes((x1,y1+ysp,xsize,ysize))
ax.set_ylim(0,13)
ax.set_xlim(0,26)
ax.plot(alpha[  0:200],qout [  0:200],label='Coupled')
ax.plot(alpha[  0:200],qoutp[  0:200],label=r'Source-only ($f(\alpha)$)')
ax.vlines(13.13, 0, 8)
#ax.plot(betab,qoutb)
ax.text(0.07*13.14,-0.19*13.14,r'Potential net photosynthesis ($10^3\alpha$)')
ax.text(0.43*13.14,-0.28*13.14,r'Potential growth ($10^3\beta$)')
ax.text(-0.54*13.14,0.89*13.14,r'Net photosynthesis ($10^3q_{in}$)',rotation='vertical')
ax.text(-0.39*13.14,0.79*13.14,r'Growth rate ($10^3q_{out}$)',rotation='vertical')
ax.text(0.06*13.14,0.92*13.14,'(a)')
ax.text(13.5,0.03*13.14,'Neutrality')
ax.legend(loc=(0.15,0.745))

ax = plt.axes((x1+xsp,y1+ysp,xsize,ysize))
ax.set_ylim(0, 1)
ax.set_xlim(0,26)
ax.plot(alpha[  0:200],dGda[  0:200],label='Coupled')
#ax.plot(betab,dGdbb)
ax.plot(alpha[  0:200],dGdap[  0:200],label=r'Source-only ($f(\alpha)$)')
ax.vlines(13.13, 0, 0.6)
ax.text(0.07*13.14,-0.19,r'Potential net photosynthesis ($10^3\alpha$)')
ax.text(0.43*13.14,-0.28,r'Potential growth ($10^3\beta$)')
ax.text(-0.39*13.14,0.50,'$q\'$',rotation='vertical')
#ax.text(0.41,0.53,r'$q\'$')
#ax.text(-0.54,0.54,r'$\partial q_{out}$ \ $\partial \alpha$',rotation='vertical')
#ax.text(-0.39,0.54,r'$\partial q_{out}$ \ $\partial \beta$',rotation='vertical')
ax.text(1.82*13.14,0.92,'(b)')
ax.text(13.5,0.03*1,'Neutrality')
ax.legend(loc='upper center')

ax = plt.axes((x1,y1,xsize,ysize))
ax.set_ylim(0,0.06)
ax.set_xlim(0,26)
for x in range(3):
  a1 = x*201
  a2 = a1+200
  print(x,a1,a2)
#  ax.plot(alpha[a1:a2],fSu[a1:a2],color=cycle[0],alpha=1/(x+1),label=r'f($\alpha$)')
ax.plot(alpha[  0:200],fSu[0:200],color=cycle[0],alpha=0.5)
ax.plot(alpha[201:401],fSu[201:401],color=cycle[0],alpha=1,label=r'$g(\alpha)|_{n = 4}$')
ax.plot(alpha[402:602],fSu[402:602],color=cycle[0],alpha=0.5)
ax.plot(alpha,fSu*0+0.0288,color=cycle[3])
#ax.plot(betab,fSub,color=cycle[1],label=r'($f\beta$)')
ax.plot(betab[  0:200],fSub[0:200],color=cycle[1],alpha=0.5)
ax.plot(betab[201:401],fSub[201:401],color=cycle[1],alpha=1,label=r'$g(\beta)|_{n = 4}$')
ax.plot(betab[402:602],fSub[402:602],color=cycle[1],alpha=0.5)
ax.vlines(13.13, 0, 0.035)
ax.text(2.01,0.052,'$n = 2$',size='8')
ax.text(0.8,0.0325,'$n = 6$',size='8')
ax.text(26.1,0.028,'$K_{Su}$',size='8')
ax.text(0.8,0.024,'$n = 6$',size='8')
ax.text(2.01,0.008,'$n = 2$',size='8')
ax.text(0.07*13.14,-0.19*0.06,r'Potential net photosynthesis ($10^3\alpha$)')
ax.text(0.49*13.14,-0.28*0.06,r'Potential growth ($10^3\beta$)')
ax.text(-0.47*13.14,0.046,r'Sucrose fraction',rotation='vertical')
ax.text(1.82*13.14,0.056,'(c)')
ax.text(13.5,0.03*0.06,'Neutrality')
ax.legend(loc='upper center')

ax = plt.axes((x1+xsp,y1,xsize,ysize))
ax.set_ylim(0, 1)
ax.set_xlim(0,26)
ax.plot(alpha[  0:200],fi[  0:200],label='Source control ($f_i$)')
ax.plot(alpha[  0:200],fa[  0:200],label='Sink control ($f_a$)')
ax.vlines(13.13, 0, 0.6)
ax.text(0.07*13.14,-0.19,r'Potential net photosynthesis ($10^3\alpha$)')
ax.text(-0.37*13.14,0.88,'Sucrose feedback (scalar)',rotation='vertical')
ax.text(1.82*13.14,0.92,'(d)')
ax.text(13.5,0.03*1,'Neutrality')
ax.legend(loc=(0.22,0.721))

plt.savefig('Figure_3.pdf')

plt.show()
