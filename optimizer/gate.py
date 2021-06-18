from math import cos, exp, sin
import math
import numpy as np
from numpy import complex

class Gate():
    def __init__(self, type, angle, qubit1=None, qubit2=None, lengthX=0.0, lengthZ=0.0, lengthCX=0.0):
        self.type=type
        self.angle=math.radians(angle)
        self.qubit1=qubit1
        self.qubit2=qubit2
        self.lengthX=0.0
        self.lengthZ=0.0
        self.lengthCX=0.0
    
    def get_matrix(self):
        if (self.type=="X"):
            return np.array([(cos(self.angle/2.0), -1j*sin(self.angle/2.0)),
                            (-1j*sin(self.angle/2.0), cos(self.angle/2.0))])
        elif (self.type=="Y"):
            return np.array([(cos(self.angle/2.0), -sin(self.angle/2.0)),
                            (sin(self.angle/2.0), cos(self.angle/2.0))])
        elif (self.type=="Z"):
            return np.array([(exp(-1j*self.angle/2.0) + sin(-1j*self.angle/2.0), 0),
                             (0, cos(1j*self.angle/2.0) + sin(1j*self.angle/2.0))])
        elif (self.type=="CX"):
            return np.array([(1, 0, 0, 0),
                            (0, 1, 0, 0),
                            (0, 0, 0, 1),
                            (0, 0, 1, 0)])
        else:
            return "Not implemented gate type"
    
    def get_time(self):
        if (self.type=="X"):
            return self.lengthX
        elif (self.type=="Z"):
            return self.lengthZ
        else:
            return 0

    def get_angle(self):
        return round(math.degrees(self.angle))
    
    def get_type(self):
        return self.type

    def to_string(self):
        if self.type != "CX":
            if self.qubit1 == None:
                return "{0}({1})".format(self.type, self.get_angle())
            else:
                return "{0}({1},{2})".format(self.type, self.qubit1, self.get_angle())
        else:
            return "{0}({1},{2})".format(self.type, self.qubit1, self.qubit2)
