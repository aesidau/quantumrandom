# Python code that relates to the notebook 
#   03_Digital operations on quantum computers
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector

# Add the operations to an algorithm that increments the number 
# encoded on a 3 qubit state vector
def add_increment(algo):
    algo.ccx(0, 1, 2) # Carry the one to qubit 2, when qubits 0 and 1 are |11>
    algo.cx(0, 1)     # Carry the one to qubit 1, when qubit 0 is |1>
    algo.x(0)         # Add one to qubit 0

q = QuantumRegister(3)    # We want 3 qubits
algo1 = QuantumCircuit(q) # Construct an algorithm on a quantum computer

# Start in the |2> row
algo1.x(1)
v1 = Statevector(algo1)
print(np.real_if_close(v1.data))

# Increment the number encoded in the state vector
add_increment(algo1)
v2 = Statevector(algo1)
print(np.real_if_close(v2.data))

# Increment the number once more
add_increment(algo1)
v3 = Statevector(algo1)
print(np.real_if_close(v3.data))

algo2 = QuantumCircuit(q) # Construct an algorithm on a quantum computer

# Start with |0> and |3> rows having equal probability
algo2.h(2)
v4 = Statevector(algo2)
print(np.real_if_close(v4.data))

# Increment the numbers encoded in the state vector
add_increment(algo2)

v5 = Statevector(algo2)
print(np.real_if_close(v5.data))
