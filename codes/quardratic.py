#This code is to display the graph and roots of the quadratic equation

from ast import increment_lineno
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import inline 

def f(x):
    return x**2-4*x-8

x=np.linspace(-3,7)
y=f(x)

result1 = fsolve(f,6)
result2 = fsolve(f,-3)

print('the roots of the equations are')
print(result1)
print(result2)

plt.grid()
plt.plot(x,y)
plt.plot(result1,f(result1),'ko')
plt.plot(result2,f(result2),'ko')
plt.title('Plotting of f(x)=$x^2-4x-8$')
alpha=format(float(result1),".8f")
beta=format(float(result2),".8f")
plt.annotate((alpha,0),(result1,f(result1)),size=10,color='grey')
plt.annotate((beta,0),(result2,f(result2)),size=10,color='grey')
plt.show()

