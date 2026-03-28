# Python code that relates to the notebook 
#   02_Other random distributions on quantum computers
# First example: bell state
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
backend = AerSimulator()

q = QuantumRegister(2)   # We want to use 2 qubits
algo = QuantumCircuit(q) # Readies us to construct an algorithm to run on the quantum computer

algo.h(0)          # Apply H operation on pairs of rows related to qubit 0
algo.cx(0,1)       # Apply CX operation, constrained where qubit 0 is |1>
algo.measure_all() # Measure the qubits and get some bits

result = backend.run(transpile(algo, backend), shots=1000).result() # Run this all 1,000 times
plot_histogram(result.get_counts())                                 # Show a histogram
plt.show()
