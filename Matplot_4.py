# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 16:19:14 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
def rad_to_degrees(x,pos):
    return round(x*57.2985,2) # round means limit the decimal digits upto 2 numbers
print(round(6.2895,2))
plt.figure(figsize=(7,5),dpi=100)
X=np.linspace(0,2*np.pi,1000) # 1000 no. betwwen 0 and 6.28
#print(X)
#print(np.linspace(0,2*np.pi,1000))
plt.plot(X,np.sin(X),'springgreen',label='sin-wave') # firstly this plots a graph between those 1000 values of randian and their sin and cosin values
#print(X,'\n\n',np.sin(X)) # list of 1000 no. b/w 0 and 6.28 and their sin values list 
plt.plot(X,np.cos(X),'magenta',label='cos-wave')
# Adjust tick position
plt.xticks(ticks=np.arange(0,370/57.2985,90/57.2985),fontsize=12,rotation=0,ha='center',va='top') # here the no. should be a little bit more than 360 to show 360 on x-axis
# Adjust tick parameters  pi=180/57.2985 hence pi/2 or 1.57072=90/57.2985 
print(np.arange(0,440/57.2985,90/57.2985)) # Here we can set the stop upto 440 because we are making step of 1.57072175 which=90 degrees
plt.tick_params(axis='both',bottom=True,top=False,left=True,right=True,direction='in',which='major',grid_color='green')
# format tick labels to convert radians into degree
formatter=FuncFormatter(rad_to_degrees) # FuncFormatter determines how the final tick label should be shown
plt.gca().xaxis.set_major_formatter(formatter) # gca() means the reference to the current axis similarly, gfa() means reference to the current figure and c in place og g stands for clear
plt.grid(linestyle='--',linewidth=0.5,alpha=0.15)
plt.legend(loc='best')
plt.title('Sine and Cosine Wave\nNotice the ticks on all 4 sides',fontsize=16)
plt.show()

