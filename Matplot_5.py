# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:56:50 2019

@author: user
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
print(mpl.rc_params()) # shows the default parameters
# This update will only be in this program and printing the mpl.rc_params() will not show the updated values 
mpl.rcParams.update({'font.size':18,'font.family':'STIXGeneral','mathtext.fontset':'stix'})
# To Go back to the default settings
#mpl.rcParams.update(mpl.rcParamsDefault)
# Print the plot atyles available
print(plt.style.available)
def plotsincosin(style='ggplot'):
    plt.style.use(style)
    plt.figure(figsize=(7,4),dpi=80)
    x=np.linspace(0,2*np.pi,1000)
    plt.plot(x,np.sin(x))
    plt.plot(x,np.cos(x))
    plt.xticks(ticks=np.arange(0,440/57.2985,90/57.2985),labels=[r'$0$',r'$90$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$'])
    plt.gca().set(ylim=(-1.25,1.25),xlim=(-.5,7),xlabel='Degrees---->',ylabel='values--->')
    plt.title(style,fontsize=18)
    plt.show()
plotsincosin('seaborn-poster')
plotsincosin('ggplot')
plotsincosin('bmh')
plotsincosin('classic')
mpl.colors.CSS4_COLORS  # 148 colors
mpl.colors.XKCD_COLORS  # 949 colors
mpl.colors.BASE_COLORS  # 8 colors