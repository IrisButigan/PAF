"""
Koristeći razvijenu klasu iz Vježbi 7 ispitajte kako domet projektila ovisi o koeficijentu trenja CD, a kako o
masi čestice. U oba slučaja fiksirajte vrijednosti svih ostalih parametara. Koristite razumne fizikalne velicine
i Runge-Kutta metodu.
"""
import matplotlib.pyplot as plt
import projectile as pro
import numpy as np

Cd = np.linspace(0.1, 0.5, 9)
M = np.linspace(1, 10, 10)
range_Cd = []
range_M = []

plt.subplot(1,2,1)

for Cd_i in Cd:
    pr = pro.Projectile(Cd = Cd_i)
    pr.gibanje_rk4()
    plt.plot(pr.x, pr.y, label='$C_d$ = {}'.format(np.around(Cd_i, 2)))
    range_Cd.append(pr.x[-1])

plt.title('Gibanje projektila za različite koeficijente trenja zraka')
plt.xlabel('x / m')
plt.ylabel('y / m') 
plt.legend()
plt.grid(True)

plt.subplot(1,2,2)

for m in M:
    pr = pro.Projectile(m = m)
    pr.gibanje_rk4()
    plt.plot(pr.x, pr.y, label='m = {} kg'.format(m))
    range_M.append(pr.x[-1])

plt.title('Gibanje projektila za različite mase')
plt.xlabel('x / m')
plt.ylabel('y / m') 
plt.legend()
plt.grid(True)
plt.show()

plt.subplot(1,2,1)
plt.xlabel('$C_d$')
plt.ylabel('D [m]')
plt.grid(True)
plt.plot(Cd, range_Cd, c = 'tab:pink')
plt.title('Ovisnost dometa o koeficijentu trenja zraka')

plt.subplot(1,2,2)
plt.xlabel('m [kg]')
plt.ylabel('D [m]')
plt.grid(True)
plt.plot(M, range_M, c = 'tab:pink')
plt.title('Ovisnost dometa o masi')
plt.show()