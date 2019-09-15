
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
plt.plot([1,2,5,9],[2,5,7,5],'g')
plt.ylabel('Some no.')
plt.axis([0,10,0,20])
plt.show()

t=np.arange(0.,5.,0.2)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
plt.title('Lines')
plt.xlabel('h')
plt.ylabel('r')
plt.legend(loc='best')
#plt.setp(lines,color='r',linewidth=3.0)
plt.show()

line,=plt.plot([1,2,5,9],[2,5,7,5],'g')
plt.axis([0,10,0,20])
line.set_antialiased(False)
plt.show()

plt.figure(figsize=(10,9)) # 15 is width and 9 is height
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'gD-', label='GreenDots')
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*-', label='Bluestars')
plt.title('A Simple Scatterplot')
plt.title('Lines')
plt.xlabel('h')
plt.ylabel('r')
plt.xlim(0,6)
plt.ylim(0,12)
plt.legend(loc='best')
plt.show()

