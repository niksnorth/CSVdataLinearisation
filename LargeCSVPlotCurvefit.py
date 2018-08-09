#############################################################################
##
## Copyright (C) 2018 Nishant Singh.
## All rights reserved.
##
#############################################################################

import matplotlib.pyplot as plt
import numpy as np
#from scipy.fftpack import fft
import tkinter as tk
from tkinter import filedialog
import time
 
#Prompt user for file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Multi Column CSV","*.csv")])
print(file_path)
 

# Load data in file: header and selected rows
tic = time.clock()
with open(file_path, "r") as data:
	line = data.readline()
	header = [e for e in line.strip().split(',') if e]
	i=0
	for i,values in enumerate(header):
		print(i,header[i])
#    print(headers
	xi=int(input("Enter 1st column index:"))
	yi=int(input("Enter 2nd column index:"))
	zi=int(input("Enter 3rd column index:"))
	ri=int(input("Enter 4th column index:"))
	si=int(input("Enter 5th column index:"))
	ti=int(input("Enter 6th column index:"))

	x, y, z, r, s, t = np.genfromtxt(data,usecols = (xi,yi,zi,ri,si,ti), delimiter=',', unpack=True)

toc = time.clock()
print("Load Time:",toc-tic)
#Plot Data
tic = time.clock()
plt.figure(1)  
plt.plot(x, r)
plt.xlabel('Time (seconds)')
plt.ylabel('Accel (g)')
plt.title(data)
plt.grid()
toc = time.clock()
print("Plot Time:",toc-tic)
plt.show(block=False)
time.sleep(10)
plt.close()
