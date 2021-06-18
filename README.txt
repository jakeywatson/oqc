OQC Tech Test
Jake Watson
18/06/2021

This repository contains the submission for the Oxford Quantum Circuits technical test.

The submission attempts to solve for the single-qubit gate reduction problems only, but does not finish or currently compile.

The optimizer.py file contains the optimisation methods. Initially, the gate sequence is condensed so that all adjacent gates of
the same type are combined into one. The gates are then multiplied together in a sliding window to identify possible identities or
equivalence to one of the Pauli matrices. This is the current failure point - comparison of complex arrays.