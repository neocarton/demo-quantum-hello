# https://qiskit.org/documentation/getting_started.html

from qiskit import (QuantumCircuit)
from qcomp import (qexec)

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)
# Add a H gate on qubit 1
circuit.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])
# Execute
qexec(circuit)
