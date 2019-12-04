# https://qiskit.org/documentation/getting_started.html

from qiskit import (QuantumRegister, ClassicalRegister, QuantumCircuit)
from qcomp import (qexec)

# Task: Control gate |00>
qr = QuantumRegister(2) # Initailly = |0>
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.cx(qr[0], qr[1]) # CNot(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Control gate |01>
qr = QuantumRegister(2) # Initailly = |0>
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[1])
circuit.cx(qr[0], qr[1]) # CNot(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Control gate |10>
qr = QuantumRegister(2) # Initailly = |0>
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[0])
circuit.cx(qr[0], qr[1]) # CNot(qr)
circuit.measure(qr, cr)
qexec(circuit)

# Task: Control gate |10>
qr = QuantumRegister(2) # Initailly = |0>
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[0])
circuit.x(qr[1])
circuit.cx(qr[0], qr[1]) # CNot(qr)
circuit.measure(qr, cr)
qexec(circuit)
