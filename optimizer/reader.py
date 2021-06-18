import re
from optimizer.gate import Gate

class Reader:

    def __init__(self, mode=1):
        self.mode=mode
        self.sequence = []
    
    def read_sequence(self, string, lengthX=0.0, lengthZ=0.0, lengthCX=0.0):
        pattern = re.compile("(X|Y|Z|CX)\((-?\d+),?(\d+)?\)")
        gates = []

        for gate in re.findall(pattern, string):
            type = gate[0]
            var1 = gate[1]
            var2 = gate[2]

            if type == "CX":
                gates.append(Gate(
                    type=type, 
                    angle=0,
                    qubit1=int(var1),
                    qubit2=int(var2),
                    lengthX=lengthX, 
                    lengthZ=lengthZ,
                    lengthCX=lengthCX))
            else:
                if var2 == "":
                    gates.append(Gate(
                        type=type, 
                        angle=int(var1),
                        qubit1=None,
                        qubit2=None,
                        lengthX=lengthX, 
                        lengthZ=lengthZ,
                        lengthCX=lengthCX))
                else:
                    gates.append(Gate(
                        type=type, 
                        angle=int(var2),
                        qubit1=int(var1),
                        qubit2=None,
                        lengthX=lengthX, 
                        lengthZ=lengthZ,
                        lengthCX=lengthCX))
        return gates





