# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 18:52:08 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(5,3),sharey=True,dpi=120)
ax1.plot([1,2,3,4,5],[2,5,9,15,20],'g--',label='greenline')
ax2.plot([1,2,3,4,5],[3,5,8,19,23],'b-',label='blueline')
ax1.set_title('Green')
ax2.set_title('Blue')
ax1.set_xlabel('x-axis')
ax2.set_ylabel('y-axis')
ax1.set_xlim(0,7)
ax2.set_xlim(0,6)
ax2.set_ylim(0,30)
plt.tight_layout()
plt.show()

# Object Oriented syntax
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(5,3),sharey=True,dpi=120)
ax1.plot([1,2,3,4,5],[2,5,9,15,20],'g--',label='greenline')
ax2.plot([1,2,3,4,5],[3,5,8,19,23],'b-',label='blueline')
ax1.set(title='Green',xlabel='x-axis',ylabel='y-axis',xlim=(0,7),ylim=(0,25),label='GreenLine')
ax2.set(title='Blue',xlabel='X-axis',ylabel='Y-axis',xlim=(0,6),label='BlueLine')
plt.tight_layout()
plt.show()

# Matlab Like syntax
plt.figure(figsize=(5,3), dpi=120) # 10 is width, 4 is height
# Left hand side plot
plt.subplot(1,2,1)  # (nRows, nColumns, axes number to plot)
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go')  # green dots
plt.title('Scatterplot Greendots')  
plt.xlabel('X'); plt.ylabel('Y')
plt.xlim(0, 6); plt.ylim(0, 12)
# Right hand side plot
plt.subplot(1,2,2)
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*')  # blue stars
plt.title('Scatterplot Bluestars')  
plt.xlabel('X'); plt.ylabel('Y')
plt.xlim(0, 6); plt.ylim(0, 12)
plt.show()

