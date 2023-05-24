import electro_magnetic as em
import numpy as np
import matplotlib.pyplot as plt

E = np.array((0, 0, 0))
B = np.array((0, 0, 1))
v = np.array((0.1, 0.1, 0.1))

qe = -1
qp = 1
m = 1

electron = em.Field(qe, m, E, B, v, 0.01)
positron = em.Field(qp, m, E, B, v, 0.01)

ax = plt.axes(projection = '3d')

x1,y1,z1 = electron.move_it()
x2,y2,z2 = positron.move_it()

ax.plot3D(x1,y1,z1)
ax.plot3D(x2,y2,z2)

plt.show()


