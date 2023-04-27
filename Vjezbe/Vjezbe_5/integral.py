import numpy as np
import calculus as calc
import matplotlib.pyplot as plt

def fja(x):
    return 2*x**2 + 3

gore = []
dolje = []
trapez = []

preciznost = np.arange(100, 900, 50) #broj pravokutnika

for i in preciznost:
    gore.append(calc.pravokutna_int(fja, 0, 1, i)[0])
    dolje.append(calc.pravokutna_int(fja, 0, 1, i)[1])
    trapez.append(calc.trapez_int(fja, 0, 1, i))


plt.title("Integrali")
plt.xlabel("N")
plt.ylabel("Vrijednost integrala")
plt.hlines(y=11/3, xmin=100, xmax=900)
plt.scatter(preciznost, trapez, label = "Metoda trapeza")
plt.scatter(preciznost, gore, label = "Gornja integralna suma")
plt.scatter(preciznost, dolje, label = "Donja integralna suma")
plt.legend()
plt.show()

