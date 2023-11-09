# Python code that relates to the notebook 
#   02_Other random distributions on quantum computers
# Second example: three outcomes with a third each
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
backend = BasicAer.get_backend('qasm_simulator')

q = QuantumRegister(2)   # We want to use 2 qubits

angle1 = 2 * np.arcsin(np.sqrt(1.0/3.0))
angle2 = np.pi / 4

algo = QuantumCircuit(q) # Readies us to construct an algorithm to run on the quantum computer

algo.ry(angle1, 1)       # Apply RY operation to swap 1/3 of qubit 1's value 
algo.h(0)                # Apply H operation on pairs of rows related to qubit 0
algo.ry(angle2, 0)       # Apply RY operation to perform a half of H on qubit 0
algo.cx(1,0)             # Apply CX operation, constrained to where qubit 1=|1>
algo.ry(-angle2, 0)      # Apply RY operation to undoing half of H on qubit 0

algo.measure_all()       # Measure the qubits and get some bits

result = execute(algo, backend, shots=1000).result() # Run this all 1,000 times
plot_histogram(result.get_counts(algo))              
plt.show()
