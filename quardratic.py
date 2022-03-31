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
print (result1)
print(result2)

plt.plot(x,y)
plt.plot(result1,f(result1),'ko')
plt.plot(result2,f(result2),'ko')
plt.title('Plotting of f(x)=$x^2-4x-8$')
plt.show()

