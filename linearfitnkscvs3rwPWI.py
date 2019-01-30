import numpy as np
import csv
import os
import sys
from collections import defaultdict
import matplotlib.pyplot as plt


# Enter filename1 to be read 

filename1 = 'exp_cfd.csv'

#filename = open('exp_cfd.csv', 'rU')
#csv = np.genfromtxt('exp_cfd.csv',delimiter=",")

x1 = []
y1 = []
#x1= np.empty_like(x)
#y1= np.empty_like(y)

columns = defaultdict(list)

#k = 1  # colno
#print(filename)
#with open('exp_cfd.csv', 'rU') as filename:
	#reader=csv.reader(filename, delimiter=",")
	
with open(filename1, 'r') as filename:
	
	reader=csv.DictReader(filename, delimiter=",")
	for row in reader:
		for (k,v) in row.items():
			columns[k].append(v)
	
filename.close()

# get x and y vectors
x1 = columns['ID']
y1 = columns['FT4']

#print(y1)
#print(y1[11])
#print(x1[35])

# convert to float type from string
x = np.empty_like(x1)
x = np.ndarray(x1)
x = x.astype(np.int)
y = np.empty_like(y1)
y = np.ndarray(y)
y = y.astype(np.float)

#test array values
#print(x)
print(x[1])
#print (columns['Radial_pos'])

# calculate polynomial
z = np.polyfit(x, y, 1)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 6)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new,'*')
plt.xlim(25000, 30000)
plt.show()

#write data file

data = np.array([x_new, y_new])
data = data.T

with open('finaldata.txt', 'w+') as datafile:
	np.savetxt(datafile, data, fmt=['%f', '%f'])



