import numpy as np
from numpy.core.defchararray import equal
from optimizer.gate import Gate


class Optimizer:

    def __init__(self, mode=1):
        self.mode=mode
    
    def optimize(self, gates):
        if self.mode == 1:

            # Begin by merging gates of the same type
            merged = []
            cumulative_angle = gates[0].get_angle()

            for i in range(1, len(gates)):
                current_type = gates[i].get_type()
                previous_type = gates[i - 1].get_type()
                current_angle = gates[i].get_angle()

                if (previous_type != current_type):
                    cumulative_angle = cumulative_angle % 360 
                    if cumulative_angle != 0:
                        merged.append(
                            Gate(
                            type=previous_type, 
                            angle=int(cumulative_angle))
                            )
                    cumulative_angle = current_angle
                else:
                    cumulative_angle += current_angle
                    if i == len(gates) - 1:
                        cumulative_angle = cumulative_angle % 360 
                        if cumulative_angle != 0:
                            merged.append(
                                Gate(
                                type=current_type, 
                                angle=int(cumulative_angle))
                                )
            window = 2
            pauli_X = np.array([(0+0j, 0-1j),
                               (0-1j, 0+0j)])
            pauli_Y = np.array([(0, -1),
                               (1,  0)])
            pauli_Z = np.array([(0-1j, 0),
                               (0, 0+1j)])
            identity = np.array([(1.0+0.0j, 0.0+0.0j),
                               (0.0+0.0j, 1.0+0j)])
            combined = []
            for i in range(1, max(len(merged) - window + 1, 1)):
                current_matrix = merged[i].get_matrix()
                equality = False

                for j in range(i + 1, min(i + window, len(merged) - 1)):
                    current_matrix = np.matmul(current_matrix, merged[j].get_matrix())
                    current_matrix.round(6)
                    print(str(i) + str(j))
                    print(current_matrix)
                    if (np.allclose(current_matrix, pauli_X) | np.allclose(current_matrix, pauli_Y) | np.allclose(current_matrix, pauli_Z | np.allclose(current_matrix, identity))):
                        if np.array_equal(current_matrix, pauli_X):
                            c_type = "X"
                        elif np.array_equal(current_matrix, pauli_Y):
                            c_type == "Y"
                        else:
                            c_type = "Z"

                        print(str(i) + "-" + str(j) + " are equal to pauli " + c_type)
                        combined.append(                                
                                    Gate(
                                    type=c_type, 
                                    angle=180))
                        equality = True
                        i = j
                if not equality:
                    combined.append(merged[i])
            return combined

                