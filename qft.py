# Python code that relates to the notebook 
#   05_Finding patterns with quantum computers
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
backend = AerSimulator()

DIRECTIONS = {0: '→', 45: '↗', 90: '↑', 135: '↖', 180: '←', 225: '↙', 270: '↓', 315: '↘'}

def direction_symbol(angle_deg):
    rounded = round(angle_deg / 45) * 45 % 360
    return DIRECTIONS.get(rounded, f'{angle_deg:.0f}°')

# Display the state vector, showing direction and magnitude for complex amplitudes.
def show_statevector(circuit, n):
    v = Statevector(circuit)
    data = v.data
    print(f"{'Row':>3}  {'State':>{n+2}}  Amplitude")
    print('-' * (n + 28))
    for i, amp in enumerate(data):
        state = f"|{format(i, f'0{n}b')}\u27e9"
        if abs(amp) < 0.001:
            val = '0'
        elif abs(amp.imag) < 0.001:
            val = f'{amp.real:+.3f}'
        else:
            mag = abs(amp)
            angle_deg = np.degrees(np.angle(amp))
            sym = direction_symbol(angle_deg)
            val = f'magnitude {mag:.3f}, direction {angle_deg:.0f}\u00b0  {sym}'
        print(f' {i:2d}  {state:>{n+2}}  {val}')

q = QuantumRegister(2)   # We want to use 2 qubits


