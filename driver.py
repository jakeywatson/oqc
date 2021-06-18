from optimizer.optimizer import Optimizer
from optimizer.reader import Reader

string1 = "X(450), Y(180), Z(-90), Z(90), X(-90), X(-180), Y(60), Y(60)"

string4 = "X(90), Y(180), Z(-90), Z(90), X(-90), X(-180), CX(1,30)"

reader = Reader()
gates = reader.read_sequence(string1)

print("Initial Sequence of Gates")
for gate in gates:
    print(gate.to_string())

optimizer = Optimizer(mode=1)
gates = optimizer.optimize(gates)

print("Final Sequence of Gates")
for gate in gates:
    print(gate.to_string())
