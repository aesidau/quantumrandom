# Python code that relates to the notebook 
#   04_Solving a problem with quantum computers
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, BasicAer
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
backend = BasicAer.get_backend('qasm_simulator')

q = QuantumRegister(3)    # We want 3 qubits
algo1 = QuantumCircuit(q) # Construct an algorithm on a quantum computer

# Start in the |3> row
algo1.x(0)
algo1.x(1)

v1 = Statevector(algo1)
print(np.real_if_close(v1.data))

# Apply CX operation, constrained to rows where qubit 0 and 1 are |1>, 
# swapping qubit 2's rows
algo1.ccx(0, 1, 2) 
v2 = Statevector(algo1)
print(np.real_if_close(v2.data))

# Verifies that a proposed solution is correct only when it is |10>
def add_verify(algo):
    algo.x(1)
    algo.ccx(0, 1, 2)
    algo.x(1)

algo2 = QuantumCircuit(q) # Construct an algorithm on a quantum computer

# Ensure the state vector has 100% in the |001> row
algo2.x(0) 

add_verify(algo2) # Add the verify function to the algorithm
v3 = Statevector(algo2)
print(np.real_if_close(v3.data))

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

algo3 = QuantumCircuit(q) # Construct an algorithm on a quantum computer
add_prepare(algo3)        # Add the operations to prepare the state vector
add_verify_with_h(algo3)  # Add the sign-flipping version of verify 
v4 = Statevector(algo3)
print(np.real_if_close(v4.data))

add_prepare(algo3)
v5 = Statevector(algo3)
print(np.real_if_close(v5.data))

# Reverses the rows of the state vector
def add_reverse(algo):
    algo.x(0)
    algo.x(1)
    algo.x(2)

add_reverse(algo3) # Add the operations to reverse the state vector
algo3.ccz(0, 1, 2) # Apply the CCZ operation to flip the sign on row |111>
add_reverse(algo3) # Add the operations to reverse the state vector again
v6 = Statevector(algo3)
print(np.real_if_close(v6.data))

add_prepare(algo3)
v7 = Statevector(algo3)
print(np.real_if_close(v7.data))

# Amplifies the row with a negative value to become more negative
def add_amplify(algo):
    add_prepare(algo)
    add_reverse(algo)
    algo.ccz(0, 1, 2)
    add_reverse(algo)
    add_prepare(algo)

c = ClassicalRegister(2)     # The solution at the end has only 2 bits
algo4 = QuantumCircuit(q, c) # Construct an algorithm on a quantum computer

add_prepare(algo4)           # Step 1 of Grover's: prepare the state vector
add_verify_with_h(algo4)     # Step 2 of Grover's: flip the solution row 
add_amplify(algo4)           # Step 3 of Grover's: amplify negative rows

algo4.measure(q[0:2], c)     # Measure the two qubits 0 and 1, get some bits
result = execute(algo4, backend, shots=1000).result() # Run this all 1,000 x
plot_histogram(result.get_counts(algo4))              # Show a histogram 
plt.show()
