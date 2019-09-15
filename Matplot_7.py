# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:41:16 2019

@author: user
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
plt.figure(figsize=(10,7),dpi=80)
x=np.linspace(0,8*np.pi,1000)
sin=plt.plot(x,np.sin(x),color='tab:blue')
# shrink= distance between the ends of box and arrow
plt.annotate('Peaks',xy=(90/57.2985,1.0),xytext=(90/57.2985,1.5),bbox=dict(boxstyle='square',fc='green',linewidth=0.1),arrowprops=dict(facecolor='r',shrink=0.01,width=0.1),fontsize=12,color='white',ha='center')
for angle in[440,810,1170]:
    # transData print the text realted to the Data provided
    plt.text(angle/57.2985,1.05,str(angle)+'\ndegrees',transform=plt.gca().transData,ha='center',color='green')
for angle in [270,630,990,1350]:
    plt.text(angle/57.2985,-1.3,str(angle)+'\ndegrees',transform=plt.gca().transData,ha='center',color='red')
plt.gca().set(xlim=(-.5,26),ylim=(-2,2))
plt.title('Annotation Examples',fontsize=18)
plt.show()
print(plt.gca().transData)

plt.figure(figsize=(14,7), dpi=80)
X = np.linspace(0, 8*np.pi, 1000)

# Text Relative to DATA
plt.text(0.50, 0.02, "Text relative to the DATA centered at : (0.50, 0.02)", transform=plt.gca().transData, fontsize=14, ha='center', color='blue')

# Text Relative to AXES
plt.text(0.50, 0.02, "Text relative to the AXES centered at : (0.50, 0.02)", transform=plt.gca().transAxes, fontsize=14, ha='center', color='blue')

# Text Relative to FIGURE
plt.text(0.50, 0.02, "Text relative to the FIGURE centered at : (0.50, 0.02)", transform=plt.gcf().transFigure, fontsize=14, ha='center', color='blue')

plt.gca().set(ylim=(-2.0, 2.0), xlim=(0, 2))
plt.title('Placing Texts Relative to Data, Axes and Figure', fontsize=18)
plt.show()

