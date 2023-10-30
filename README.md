# quantumrandom
Notebooks that explore how to use quantum computers to create random numbers

This set of Jupyter Notebooks is to support my blog posts on getting starting with quantum computing. I wanted to see if 
I could explain quantum computing without having to use [Bloch Spheres](https://en.wikipedia.org/wiki/Bloch_sphere) or
[circuit notation](https://en.wikipedia.org/wiki/Quantum_circuit), since I feel these create a false intuition around how 
qubits work. For instance, Bloch Spheres do not show entanglement, and circuit notation implies control travelling in one
direction so misses phase kickbacks. I also want to avoid using deep mathematics (by which I mean the combination of 
[Dirac notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation), complex numbers and 
[linear algebra](https://en.wikipedia.org/wiki/Linear_algebra)), and while this is the most accurate representation, it 
makes the topic inaccessible for many.

The [IBM Qiskit](https://qiskit.org/) quantum computing library is used for the code exercises in the notebooks, as it is
widely available, free to use, and produces appropriate visualisations in a Jupyter Notebook environment. There are other
quantumn computing libraries that might also have been used, and it should be easy to convert the code exercises if anyone
wants to do that.

Here are direct links to the notebooks:
1. [Context](https://github.com/aesidau/quantumrandom/blob/main/00_Context.ipynb) - the motivations for these notebooks and instructions on how to set up the environment for those that wish to run them themselves.
2. [A simple algorithm](https://github.com/aesidau/quantumrandom/blob/main/01_A%20simple%20and%20useful%20quantum%20algorithm.ipynb) - how to use a quantum computer to generate real random bits
3. [More complex randomness](https://github.com/aesidau/quantumrandom/blob/main/02_Other%20random%20distributions%20on%20quantum%20computers.ipynb) - how to generate non-uniform distributions of random bits
4. [Digital computation](https://github.com/aesidau/quantumrandom/blob/main/03_Digital%20operations%20on%20quantum%20computers.ipynb) - how to perform traditional digital computation on a quantum computer
5. [Grover's algorithm](https://github.com/aesidau/quantumrandom/blob/main/04_Solving%20a%20problem%20with%20quantum%20computers.ipynb) - how to use a quantum computer to find a solution that would require brute-forcing on a digital computer

If you want to just read the material, jump straight to the [simple algorithm notebook](https://github.com/aesidau/quantumrandom/blob/main/01_A%20simple%20and%20useful%20quantum%20algorithm.ipynb).

These notebooks are also a proof-of-concept for how a quantum computing course or book might be developed that doesn't use circuit notation, Bloch Spheres, complex numbers or linear algebra. However, there is some highschool-level mathematics involved, such as fractions, square roots, and addition/multiplication.

Enjoy!