import harmonic_oscillator as ho
import numpy as np
import matplotlib.pyplot as plt

x0 = 0.3
v0 = 0
k = 10
m = 0.1

t_an = np.linspace(0, 2, 10000)
x_an = x0 * np.cos(np.sqrt(k/m) * t_an)
plt.plot(t_an, x_an, label = 'analitycal')
print('Analitički period iznnosi {} s'.format(2*np.pi*np.sqrt(m/k)))

dt = [0.001, 0.01, 0.05]

for dt_i in dt:
    ho_i = ho.Oscillator(m, k, x0, v0, dt_i)
    t, x = ho_i.move_it()
    print('Numerički period za dt = {0} iznnosi {1} s'.format(dt_i, ho_i.period()))
    plt.scatter(t, x, label = 'dt = {}'.format(dt_i), s = dt_i * 100)

plt.legend(loc = 4)
plt.show()