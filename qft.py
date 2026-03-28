# Python code that relates to the notebook 
#   05_Finding patterns with quantum computers
import numpy as np
from fractions import Fraction
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.visualization import plot_histogram, array_to_latex
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
backend = AerSimulator()

DIRECTIONS = {0: '→', 45: '↗', 90: '↑', 135: '↖', 180: '←', 225: '↙', 270: '↓', 315: '↘'}

def direction_symbol(angle_rad):
    angle_deg = np.degrees(angle_rad) % 360
    rounded = round(angle_deg / 45) * 45 % 360
    return DIRECTIONS.get(rounded, '?')

def angle_to_pi_str(angle_rad):
    """Convert a radian angle to a π-fraction string (e.g. π/2, -3π/4).
    Falls back to a decimal radian value if the angle is not a clean fraction of π."""
    if abs(angle_rad) < 1e-9:
        return '0'
    ratio = angle_rad / np.pi
    frac = Fraction(ratio).limit_denominator(64)
    if abs(float(frac) - ratio) > 1e-9:
        return f'{angle_rad:.4f}'
    num, den = frac.numerator, frac.denominator
    if den == 1:
        if num == 1:  return 'π'
        if num == -1: return '-π'
        return f'{num}π'
    if num == 1:  return f'π/{den}'
    if num == -1: return f'-π/{den}'
    return f'{num}π/{den}'

def show_statevector(algo, n):
    """Display the state vector, showing direction and magnitude for complex amplitudes."""
    v = Statevector(algo)
    data = v.data
    print(f"{'Row':>3}  {'State':>{n+2}}  Amplitude")
    print('-' * (n + 28))
    for i, amp in enumerate(data):
        state = f"|{format(i, f'0{n}b')}⟩"
        if abs(amp) < 0.001:
            val = '0'
        elif abs(amp.imag) < 0.001:
            val = f'{amp.real:+.3f}'
        else:
            mag = abs(amp)
            angle_rad = np.angle(amp)
            sym = direction_symbol(angle_rad)
            val = f'magnitude {mag:.3f}, direction {angle_to_pi_str(angle_rad)}  {sym}'
        print(f' {i:2d}  {state:>{n+2}}  {val}')

algo1 = QuantumCircuit(1)
algo1.h(0)
print('After H:')
show_statevector(algo1, 1)

print()

algo1.p(np.pi / 2, 0)   # P(π/2) — rotate |1⟩ row by π/2
print('After P(π/2):')
show_statevector(algo1, 1)

# Uniform pattern: both rows have the same value.
# H creates it, then H again detects it — collapses to row 0.
algo2 = QuantumCircuit(1)
algo2.h(0)  # creates uniform probability distribution
algo2.h(0)  # H detects the uniform pattern
print('Uniform pattern → H detects frequency 0 (no repeating pattern):')
show_statevector(algo2, 1)

print()

# Alternating pattern: rows have opposite signs.
# X followed by H creates (|0> - |1>)/√2. H then detects it — collapses to row 1.
algo3 = QuantumCircuit(1)
algo3.x(0)   # |1>
algo3.h(0)   # creates (|0> - |1>)/√2: an alternating pattern
algo3.h(0)   # H detects the alternating pattern
print('Alternating pattern → H detects frequency 1 (period 2):')
show_statevector(algo3, 1)

def add_qft(algo, qubits):
    """Apply the Quantum Fourier Transform to the specified qubits."""
    n = len(qubits)
    for i in range(n - 1, -1, -1):
        algo.h(qubits[i])
        for j in range(i - 1, -1, -1):
            angle = np.pi / 2 ** (i - j)
            algo.cp(angle, qubits[j], qubits[i])
    for i in range(n // 2):
        algo.swap(qubits[i], qubits[n - 1 - i])

# Prepare a period-2 state: non-zero at rows 0, 2, 4, 6
algo4 = QuantumCircuit(3)
algo4.h(1)
algo4.h(2)

print('Period-2 state (non-zero at rows 0, 2, 4, 6):')
show_statevector(algo4, 3)

# Now we apply the QFT to this periodic state and inspect what comes out.
add_qft(algo4, [0, 1, 2])

print('After QFT:')
show_statevector(algo4, 3)

# Measure and run
algo5 = QuantumCircuit(3)
algo5.h(1)
algo5.h(2)
add_qft(algo5, [0, 1, 2])
algo5.measure_all()

result = backend.run(transpile(algo5, backend), shots=1000).result()
counts = result.get_counts()
print('Measurement results:', counts)
plot_histogram(counts)
plt.show()
