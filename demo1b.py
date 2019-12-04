# https://qiskit.org/documentation/getting_started.html

from qiskit import (QuantumRegister, ClassicalRegister, QuantumCircuit)
from qcomp import (qexec)

# Task: Put |0> into superposition
qr = QuantumRegister(1) # Initailly = |0>
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.h(qr) # H(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Put QuBit in superposition back to previous state |0>
qr = QuantumRegister(1) # Initailly = |0>
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.h(qr) # H(qr)
circuit.h(qr) # H(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Put |1> into superposition
qr = QuantumRegister(1) # Initailly = |0>
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr) # Not(qr)
circuit.h(qr) # H(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Put QuBit in superposition back to previous state |1>
qr = QuantumRegister(1) # Initailly = |0>
cr = ClassicalRegister(1)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr) # Not(qr)
circuit.h(qr) # H(qr)
circuit.h(qr) # H(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Application of double h(qr)? Restore quantum state?
