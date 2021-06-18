class Sequence:

    def __init__(self):
        self.gates=[]
        self.gate_number = len(self.gates)

    def add_gate(self, gate):
        self.gates.append(gate)
    
    def set_gates(self, sequence):
        self.gates = sequence
    
    def get_time(self):
        time = 0
        for gate in self.gates:
            time += gate.get_time()
        return time
