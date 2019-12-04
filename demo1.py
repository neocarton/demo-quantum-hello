# https://qiskit.org/documentation/getting_started.html

from qiskit import (QuantumRegister, ClassicalRegister, QuantumCircuit)
from qcomp import (qexec)

# Create a Quantum Circuit acting on the q register
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)
# Add a H gate on qubit 1
circuit.h(qr[0])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(qr[0], qr[1])
# Map the quantum measurement to the classical bits
circuit.measure(qr, cr)
# Execute
qexec(circuit)
