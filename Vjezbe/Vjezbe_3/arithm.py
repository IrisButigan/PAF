import numpy as np
#a
def aritmeticka(br):
    suma = sum(br)
    n = len(br)
    return suma/n

def devijacija(br):
    arit = aritmeticka(br)
    suma = 0
    for b in br:
        suma += (b - arit)**2
    n = len(br)
    dev = np.sqrt(suma/(n*(n-1)))
    return dev

brojevi = [1,2,3,4,5,6,7,8,9,10]
print("Prosjecna vrijednost je: {}".format(aritmeticka(brojevi)))
print("Standardna devijacija je: {}".format(devijacija(brojevi)))

#b
print("Prosjecna vrijednost je: {}".format(np.average(brojevi)))
print("Standardna devijacija je: {}".format(np.std(brojevi)*np.sqrt(1/9))) #nazivnik u np.std je n(10) pa mnozimo s sqrt(1/9)
#ili
import statistics as stat
print("Prosjecna vrijednost je: {}".format(stat.mean(brojevi)))
print("Standardna devijacija je: {}".format(stat.stdev(brojevi)*np.sqrt(1/10))) #nazivnik u np.std je n-1(9) pa mnozimo s sqrt(1/10)   