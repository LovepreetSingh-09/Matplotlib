# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:41:23 2019

@author: user
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
# Scatterplot with varying size and color of points
import pandas as pd
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")
print(midwest)
# Plot
fig = plt.figure(figsize=(9, 5), dpi= 80, facecolor='w', edgecolor='green')    
plt.scatter('area', 'poptotal', data=midwest, s='dot_size', c='popdensity', cmap='gist_rainbow', edgecolors='blue', linewidths=0.5)
plt.title("Bubble Plot of PopTotal vs Area\n(color: 'popdensity' & size: 'dot_size' - both are numeric columns in midwest)", fontsize=16)
plt.xlabel('Area', fontsize=18)
plt.ylabel('Poptotal', fontsize=18)
plt.colorbar()
plt.show() 

midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")
print(midwest)
# Plot
fig = plt.figure(figsize=(14, 9), dpi= 80, facecolor='w', edgecolor='g')    
colors = plt.cm.tab20.colors
print(colors)
categories = np.unique(midwest['category'])
print(categories)
 # means the location of data under the catgory column category act on row and all the data under this element
for i, category in enumerate(categories): # enumerate makes an object and provides the index no. to reach element  
    plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category==category, :], s='dot_size', c=colors[i], label=str(category), edgecolors='black', linewidths=.5)
    print(midwest.loc[midwest.category==category, :]) # midwest.loc[midwest.category==category, :] represent the location of the data of the row related to each of the category one by one, like county, state,dotsize,popdensity etc
# Legend for size of points
for dot_size in [100, 300, 600]:
    plt.scatter([], [], c='k', alpha=0.5, s=dot_size, label=str(dot_size) + ' TotalPop')
plt.legend(loc='upper right', scatterpoints=1, frameon=True, labelspacing=2, title='Saravana Stores', fontsize=8)
plt.title("Bubble Plot of PopTotal vs Area\n(color: 'category' - a categorical column in midwest)", fontsize=18)
plt.xlabel('Area', fontsize=16)
plt.ylabel('Poptotal', fontsize=16)
plt.show()     