import numpy as np
import matplotlib.pyplot as plt

class Field:
    def __init__(self, q, m, E, B, v0, dt):
        self.q = q
        self.m = m
        self.E = E
        self.B = B
        self.v0 = v0
        self.dt = dt

    def start(self):
        self.t = [0]
        #self.r = [[0,0,0]]
        self.v = self.v0
        #self.a = [[0,0,0]]
        self.x = [0]
        self.y = [0]
        self.z = [0]

    def __move(self):
        self.a = self.q * (self.E + np.cross(self.v, self.B)) / self.m
        self.v += self.a * self.dt
        #self.r.append(self.r[-1] + self.v * self.dt)
        self.x.append(self.x[-1] + self.v[0] * self.dt)
        self.y.append(self.y[-1] + self.v[1] * self.dt)
        self.z.append(self.z[-1] + self.v[2] * self.dt)
        self.t.append(self.t[-1] + self.dt)

    def move_it(self, trajanje = 20):
        self.start()
        while self.t[-1] <= trajanje:
            self.__move()
         return self.x, self.y, self.z
    