# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 23:09:30 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed,randint
seed(100)
fig,axes=plt.subplots(3,2,figsize=(5,5),sharex=False,dpi=120)
colors={0:'g',1:'y',2:'b',3:'k',4:'r',5:'g'}
markers={0:'o',1:'*',2:'D',3:'p',4:'o',5:'*'}
for i,ax in enumerate(axes.ravel()):
    ax.plot(sorted(randint(0,10,10)),sorted(randint(0,10,10)),marker=markers[i],color=colors[i])
    ax.set_title('Ax:'+str(i))
    ax.yaxis.set_ticks_position('none') # for hiding the ticks on the y axis
    
plt.suptitle('Four sub plots',verticalalignment='bottom',fontsize=16)
plt.tight_layout()
plt.show()

print(axes) # an array consists of arrays of no. of rows and then each array of these arrays contains no. of the object in that row like here its array has 3 arrays which contains 2 objects
print(axes.ravel())# make that no. of arrays into a single array consists of all the elements
print(enumerate(axes.ravel()))# enumerate means making a single object containing the info of axes like no.(0,1,2,3,4,5) and location
for i,ax in enumerate(axes.ravel()):
    print(ax)
    
#output of ax :- which gives the location in vertical position(column),horizontal position(rows),size of the each graph 
#AxesSubplot(0.0671528,0.566898;0.398889x0.313657)
#AxesSubplot(0.565278,0.566898;0.398889x0.313657)
#AxesSubplot(0.0671528,0.124074;0.398889x0.313657)
#AxesSubplot(0.565278,0.124074;0.398889x0.313657)
from matplotlib.ticker import FuncFormatter

def rad_to_degrees(x, pos):
    'converts radians to degrees'
    return round(x * 57.2985, 2)

plt.figure(figsize=(12,7), dpi=100)
X = np.linspace(0,2*np.pi,1000)
plt.plot(X,np.sin(X))
plt.plot(X,np.cos(X))

# 1. Adjust x axis Ticks
plt.xticks(ticks=np.arange(0, 440/57.2985, 90/57.2985), fontsize=12, rotation=30, ha='center', va='top')  # 1 radian = 57.2985 degrees

# 2. Tick Parameters
plt.tick_params(axis='both',bottom=True, top=True, left=True, right=True, direction='in', which='major', grid_color='blue')

# 3. Format tick labels to convert radians to degrees
formatter = FuncFormatter(rad_to_degrees)
plt.gca().xaxis.set_major_formatter(formatter)

plt.grid(linestyle='--', linewidth=0.5, alpha=0.15)
plt.title('Sine and Cosine Waves\n(Notice the ticks are on all 4 sides pointing inwards, radians converted to degrees in x axis)', fontsize=14)
plt.show()