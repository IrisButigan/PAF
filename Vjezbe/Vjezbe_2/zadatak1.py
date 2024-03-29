import numpy as np
import matplotlib.pyplot as plt
sila = int(input("iznos sile u N: "))
masa = int(input("iznos mase u kg: "))
akc = sila/masa
t = 10
brz = akc*t
put = 0.5*akc*t**2
vremena=np.linspace(0,t,100)

plt.subplot(1,3,1)
plt.title("a-t graf")
plt.xlabel("t [s]")
plt.ylabel("a [m/s^2]")
plt.hlines(y=akc, xmin=0, xmax=t)

plt.subplot(1,3,2)
plt.title("v-t graf")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
brzine=vremena*akc
plt.plot(vremena, brzine)

plt.subplot(1,3,3)
plt.title("x-t graf")
plt.xlabel("t [s]")
plt.ylabel("x [m]")
putevi = 0.5*akc*vremena**2
plt.plot(vremena, putevi)
plt.show()