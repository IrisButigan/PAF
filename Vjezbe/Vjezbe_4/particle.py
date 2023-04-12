import numpy as np
class Particle:
    def __init__(self, v0, kut_otklona, x, y, dt = 0.01):
        self.v0 = v0
        self.kut_otklona = kut_otklona * np.pi / 180
        self.x = x
        self.y = y
        self.dt = dt

    def printInfo(self):
        print("početna brzina čestice je: ", self.v0)
        print("kut otklona čestice je: ", self.kut_otklona * 180 / np.pi)
        print("x koordinata početnog položaja je: ",  self.x)
        print("y koordinata početnog položaja je: ",  self.y)
    
    def moveToOrigin(self):
        self.x=0
        self.y=0
    
    def range_analiticki(self):
        return(2*self.v0*np.cos(self.kut_otklona)*self.v0*np.sin(self.kut_otklona)/9.81)
    
    def reset(self):
        self.v0 = 0
        self.kut_otklona = 0
        self.x = 0
        self.y = 0

    def __move(self):
        self.v_x = []
        self.v_y = []
        self.v0_x = self.v0 * np.cos(self.kut_otklona)
        self.v0_y = self.v0 * np.sin(self.kut_otklona) - 9.81*self.dt
        self.v_x.append(self.v0_x)
        self.v_y.append(self.v0_y)

        self.x2 = []
        self.y2 = []
        self.x0 = self.v0_x*self.dt
        self.y0 = self.v0_y*self.dt
        self.x2.append(self.x0)
        self.y2.append(self.y0)
        self.vrijeme = []

        i = len(self.v_x)
        self.x2.append(self.x2[i-1] + self.v_x[i]*self.dt)
        self.y2.append(self.y2[i-1] + self.v_y[i]*self.dt)
        self.v_x.append(self.v0_x)
        self.v_y.append(self.v_y[i-1] - 9.81*self.dt)
        self.vrijeme.append(self.dt)

    def range(self):
        self.v_x = []
        self.v_y = []
        self.v0_x = self.v0 * np.cos(self.kut_otklona)
        self.v0_y = self.v0 * np.sin(self.kut_otklona) - 9.81*self.dt
        self.v_x.append(self.v0_x)
        self.v_y.append(self.v0_y)

        self.x2 = []
        self.y2 = []
        self.x0 = self.v0_x*self.dt
        self.y0 = self.v0_y*self.dt
        self.x2.append(self.x0)
        self.y2.append(self.y0)
        self.vrijeme = []
        range = 0
        i = 0
        y_d = self.y
        while y_d >= 0:
            self.x2.append(self.x2[i-1] + self.v_x[i-1]*self.dt)
            self.y2.append(self.y2[i-1] + self.v_y[i-1]*self.dt)
            self.v_x.append(self.v0_x)
            self.v_y.append(self.v_y[i-1] - 9.81*self.dt)
            self.vrijeme.append(self.dt)            

            y_d = self.y2[i]
            range = self.x2[i]
            i = i + 1
        return range

        

    
        
    
