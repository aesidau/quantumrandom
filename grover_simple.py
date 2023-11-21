# Python code that relates to the notebook 
#   04_Solving a problem with quantum computers
# Simplified, so is just the parts to perform Grover's algorithm on 3 qubits
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
backend = BasicAer.get_backend('qasm_simulator')

# Verifies that a proposed solution is correct only when it is |10>
# ** Change this function to have Grover's produce a different result
def add_verify(algo):
    algo.x(1)
    algo.ccx(0, 1, 2)
    algo.x(1)

# Flips the sign of the row corresponding to the outcome that 
# the verify function would indicate is correct
def add_verify_with_h(algo):
    algo.h(2)
    add_verify(algo)
    algo.h(2)

# Creates a uniform probability distribution across the state vector
def add_prepare(algo):
    algo.h(0)
    algo.h(1)
    algo.h(2)

# Reverses the rows of the state vector
def add_reverse(algo):
    algo.x(0)
    algo.x(1)
    algo.x(2)

# Amplifies the row with a negative value to become more negative
def add_amplify(algo):
    add_prepare(algo)
    add_reverse(algo)
    algo.ccz(0, 1, 2)
    add_reverse(algo)
    add_prepare(algo)

q = QuantumRegister(3)       # We want 3 qubits
c = ClassicalRegister(2)     # The solution at the end has only 2 bits
algo4 = QuantumCircuit(q, c) # Construct an algorithm on a quantum computer

add_prepare(algo4)           # Step 1 of Grover's: prepare the state vector
add_verify_with_h(algo4)     # Step 2 of Grover's: flip the solution row 
add_amplify(algo4)           # Step 3 of Grover's: amplify negative rows

algo4.measure(q[0:2], c)     # Measure the two qubits 0 and 1, get some bits
result = execute(algo4, backend, shots=1000).result() # Run this all 1,000 x
plot_histogram(result.get_counts(algo4))              # Show a histogram 
plt.show()
