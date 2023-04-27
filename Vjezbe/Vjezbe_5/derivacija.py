import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def fja(x):
   f = 5*x**3-2*x**2+2*x+3
   return f

def der_fja(x):
   d = 5*3*x**2-2*2*x+2
   return d

eps1 = calc.der_raspon(fja, -2, 2, h = 0.01)
eps2 = calc.der_raspon(fja, -2, 2, h = 0.1)

tocke = np.arange(-2, 2, 0.1)
analiticka_derivacija = der_fja(tocke)

plt.title("Derivacije")
plt.xlabel("x")
plt.ylabel("f´(x)")
plt.plot(tocke, analiticka_derivacija, label = "analitička derivacija")
plt.plot(eps1[0], eps1[1], label = "epsilon = 0.01")
plt.plot(eps2[0], eps2[1], label = "epsilon = 0.1")
plt.legend()
plt.show()