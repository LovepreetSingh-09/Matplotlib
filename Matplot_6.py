# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:27:28 2019

@author: user
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
print(mpl.colors.CSS4_COLORS)  # 148 colors
print(mpl.colors.XKCD_COLORS)  # 949 colors
print(mpl.colors.BASE_COLORS)  # 8 colors
plt.figure(figsize=(10,7),dpi=80)
x=np.linspace(0,8*np.pi,1000)
sin=plt.plot(x,np.sin(x))
cos=plt.plot(x,np.cos(x))
sin1=plt.plot(x,np.sin(x+.5))
cos1=plt.plot(x,np.cos(x+.5))
plt.gca().set(xlim=(-.5,7),ylim=(-1.25,1.5))
plt.title('Legend example',fontsize=18)
plt.legend([sin[0],cos[0],sin1[0],cos1[0]],['Sin-curve','Cos-curve','Sin1-curve','Cos1-curve'],frameon=True,framealpha=1,ncol=2,shadow=True,borderpad=1,title='Sin and Cos Waves')
# alpha=the color in the range 0 and 1 0=black and 1= white and 0.5=grey 
plt.show()