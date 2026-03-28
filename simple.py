# Python code that relates to the notebook 
#   01_A simple and useful quantum algorithm.ipynb
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
backend = AerSimulator()

q = QuantumRegister(2)   # We want to use 2 qubits
algo = QuantumCircuit(q) # Readies us to construct an algorithm to run on the quantum computer

v1 = Statevector(algo)
print(np.real_if_close(v1.data)) # Or array_to_latex(np.vstack(v1.data))

algo.h(0)  # Apply H operation on pairs of rows related to qubit 0
v2 = Statevector(algo)
print(np.real_if_close(v2.data))

algo.h(1)  # Apply H operation on pairs of rows related to qubit 1
v3 = Statevector(algo)
print(np.real_if_close(v3.data))

algo.measure_all()  # Measure the qubits and get some bits

result = backend.run(transpile(algo, backend), shots=1000).result()  # Run this all 1,000 times
plot_histogram(result.get_counts())
plt.show()
