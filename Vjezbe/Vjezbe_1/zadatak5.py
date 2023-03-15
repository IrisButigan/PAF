import matplotlib.pyplot as plt
import numpy as np



def pravac(x1, y1, x2, y2):
    if x1 != x2:
        a = (y2 - y1)/(x2 - x1)
        b = - a * x1 + y1
        print("Pravac y = {}x + {}".format(a, b))
    else:
        print("Pravac x = {}".format(x1))
    
    x = np.linspace(0, 10, 100)
    y = a*x + b

    plt.title("Pravac kroz dvije točke")
    plt.xlabel("X-os")
    plt.ylabel("Y-os")

    plt.plot(x, y)
    plt.plot(x1, y1, marker="*")
    plt.plot(x2, y2, marker="*")
    
    odabir = int(input("Prikaži na ekranu [1] ili spremi kao PDF [2]: "))
    if odabir == 1:
        plt.show()
    elif odabir == 2:
        ime = input("Ime pod kojim će se spremiti graf: ")
        ime += ".pdf"
        plt.savefig(ime)
    else:
        print("Pogreška")


    

pravac(1,2,3,4)
