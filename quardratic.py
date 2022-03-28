#This code is to display the graph

import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b,c):
    return a*x**2+b*x+c

xlist=np.linspace(-3,7,num=100)
ylist=f(xlist,1,-4,-8)

plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
plt.plot(xlist,ylist**0-1,'--g')
plt.title("plotting of f(x)=$x^2-4x-8$")
plt.show()