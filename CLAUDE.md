# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an educational quantum computing project — a series of Jupyter Notebooks that teach quantum computing concepts without Bloch Spheres, circuit notation, or deep mathematics (Dirac notation, complex numbers, linear algebra). It uses [IBM Qiskit](https://qiskit.org/) with a local simulator.

## Running the code

**Notebooks** (primary format):
```
jupyter notebook
```

**Standalone Python scripts** (run from the repo root):
```
python simple.py
python bellstate.py
python thirds.py
python increment.py
python grover_simple.py
python grover.py
```

Scripts produce matplotlib histogram plots using `plt.show()` — requires a display environment.

## Dependencies

The code uses `qiskit` with `qiskit-aer` as the local simulator backend:
```python
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
backend = AerSimulator()
```

State vector inspection uses `qiskit.quantum_info.Statevector`, and visualization uses `qiskit.visualization.plot_histogram` + `matplotlib`.

## Project structure

Each notebook has a corresponding standalone `.py` script that extracts the runnable code:

| Notebook | Script | Topic |
|---|---|---|
| `00_Context.ipynb` | — | Setup and motivation |
| `01_A simple and useful quantum algorithm.ipynb` | `simple.py` | Random bit generation with H gates |
| `02_Other random distributions on quantum computers.ipynb` | `bellstate.py`, `thirds.py` | Bell states, non-uniform distributions |
| `03_Digital operations on quantum computers.ipynb` | `increment.py` | Classical digital ops on quantum hardware |
| `04_Solving a problem with quantum computers.ipynb` | `grover.py`, `grover_simple.py` | Grover's algorithm |
| `05_Finding patterns with quantum computers.ipynb` | — | Quantum Fourier Transform, period finding |

`grover_simple.py` is a stripped-down version of `grover.py` without intermediate state vector printouts — useful as a clean template for modifying the `add_verify` function to search for different targets.

## Teaching principles

These principles govern how new content should be written or extended:

1. **Motivation before mechanics.** Every concept is introduced with a real-world reason to care (cryptographic randomness, search problems, password checking) before the operational details are given.

2. **Operational framing over mathematical formalism.** Operations are described by what they *do* to rows of the state vector — not by their matrix representation, eigenvalues, or physics interpretation. The question is always "what changes, and how?"

3. **Concrete tables as the primary explanatory tool.** State vector transformations are shown step-by-step in tables. Readers should be able to trace every value change by hand.

4. **Progressive complexity with explicit bridges.** Each notebook opens by referencing what was established previously and explains why the next concept is a natural extension. Complexity is never introduced without a connecting sentence.

5. **Analogies grounded in everyday experience.** Abstract ideas are anchored to familiar things: the coin-flipping robot (qubit vs. bit), coins always landing matched (Bell state), carrying a digit when counting (increment circuit).

6. **Demystify the strange early.** Negative probability amplitudes are introduced in notebook 02, not deferred. Directional (complex) amplitudes are introduced in notebook 05 using a clock-hand analogy rather than complex number notation. Strangeness is named and defused, not avoided.

7. **Deliberate vocabulary.** Physics jargon (superposition, entanglement, interference) is avoided. Quantum circuit terminology (circuit, gate) is avoided. Operations get plain names: H is "half," CX is "constrained swap," CCX is "doubly constrained swap," Z is "flip," P is "phase rotation," CP is "constrained phase rotation." These names reflect what the operation does, not its physics origin.

8. **Accumulating summary tables.** Each notebook ends with (or contributes to) a reference table of all operations introduced so far — name, short description, and detailed description. The table grows across notebooks, reinforcing prior learning.

9. **Explicit acknowledgment of simplifications.** When a loose definition or non-standard usage is intentional, it is called out directly. Readers are told they will gain rigor later from other sources; the goal here is correct intuition first.

10. **Show the algorithm working, then explain why.** Code is run and output is shown before the mechanism is fully explained. Seeing the result first gives readers a concrete target for the explanation that follows.

## Qiskit patterns used

State vector inspection mid-circuit (for educational printouts):
```python
v = Statevector(algo)
print(np.real_if_close(v.data))
```

Displaying complex amplitudes as magnitude + compass direction (notebook 05):
```python
DIRECTIONS = {0: '→', 45: '↗', 90: '↑', 135: '↖', 180: '←', 225: '↙', 270: '↓', 315: '↘'}

def show_statevector(circuit, n):
    v = Statevector(circuit)
    for i, amp in enumerate(v.data):
        # shows "+0.707" for real values, "magnitude 0.707, direction 90°  ↑" for complex
```

Grover's algorithm structure in `grover_simple.py`:
1. `add_prepare` — uniform superposition via H gates
2. `add_verify_with_h` — phase kickback to flip sign of target row
3. `add_amplify` — amplitude amplification (prepare → reverse → CCZ → reverse → prepare)

QFT structure in notebook 05:
1. `add_qft` — H gates + CP phase rotations + SWAP to reverse qubit order
