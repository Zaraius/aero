from matplotlib import pyplot as plt
import numpy as np
from random import random
from scipy.constants import g
from math import pi, sin, cos

class PositionGraph:
    dt = 0.1
    a, v, vi, dx, va, r = [[0,0,0] for i in range(6)]
    X = [[0], [0], [0]]
    

    def __init__(self, dt):
        self.dt = dt
        
    
    def new_input(self, ax, ay, az, vax, vay, vaz):
        self.a = [ax, ay, az]
        self.va = [vax, vay, vaz]

        #Calculate distance, rotation in each dimension + unit conversions
        for dim in range(3):
            self.a[dim] /= g
            self.vi[dim] = self.v[dim]
            self.v[dim] = self.vi[dim] + self.a[dim]*self.dt
            self.dx[dim] = self.vi[dim]*self.dt + 0.5*self.a[dim]*pow(self.dt,2)

            self.va[dim] *= pi/180
            self.r[dim] += self.va[dim]*self.dt
        #create rotational matrices and adjust positions accordingly
        Rx = np.array([[1, 0, 0], [0, cos(self.r[0]), -sin(self.r[0])], [0, sin(self.r[0]), cos(self.r[0])]]) #roll
        Ry = np.array([[cos(self.r[1]), 0, sin(self.r[1])], [0, 1, 0], [-sin(self.r[1]), 0, cos(self.r[1])]]) #pitch
        Rz = np.array([[cos(self.r[2]), -sin(self.r[2]), 0], [sin(self.r[2]), cos(self.r[2]), 0], [0, 0, 1]]) #yaw
        pos = Rx @ Ry @ Rz @ np.array([[self.dx[0]], [self.dx[1]], [self.dx[2]]])
        pos = pos.tolist()

        for dim in range(3):
            self.X[dim].append(self.X[dim][len(self.X[dim])-1] + pos[dim][0])
        
        return self.X