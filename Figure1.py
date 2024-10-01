import matplotlib.pyplot as plt
import numpy as np

#https://www.tutorialspoint.com/how-to-add-leading-zeros-to-a-number-in-python#:~:text=One%20method%20to%20add%20leading,that%20will%20come%20as%20output.
desired_width = 4
name = 'OUTPUT/diag_'
ext = '.txt'

num = 11
for number in range(1,num):
	number_str = "{:0>{}}".format(number, desired_width)
	#print("Number after leading zeros: ") 
	#print(number_str)
	filename = name + number_str + ext
	print (filename)
	i, fSu = np.loadtxt(filename, unpack=True)
	plt.plot (i, fSu, color='C0')

#plt.legend()

plt.xlabel('Time (day)')
plt.ylabel('Sucrose concentration (fraction of DM)')

# For rasterized output.
plt.savefig('Figure1.png')

# For vectorized output.
plt.savefig('Figure1.pdf')

plt.show()
