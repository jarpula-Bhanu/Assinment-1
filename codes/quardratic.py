import numpy as np
import matplotlib.pyplot as plt

coeff=[1,-4,-8]
print('The roots of the equation are ')
print(np.roots(coeff))

x=np.linspace(-3,7)
y=x**2-4*x-8

plt.grid()
plt.plot(x,y)
plt.plot(np.roots(coeff)[0],0,'ko')
plt.plot(np.roots(coeff)[1],0,'ko')
plt.title('Plotting of f(x)=$x^2-4x-8$')
alpha=format(float(np.roots(coeff)[0]),".8f")
beta=format(float(np.roots(coeff)[1]),".8f")
plt.annotate((alpha,0),(np.roots(coeff)[0],0),size=10,color='grey')
plt.annotate((beta,0),(np.roots(coeff)[1],0),size=10,color='grey')
plt.show()
