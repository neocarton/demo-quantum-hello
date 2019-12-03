# https://qiskit.org/documentation/getting_started.html

import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

def myexe(circuit) :
    # Use Aer's qasm_simulator
    backend = Aer.get_backend('qasm_simulator')
    # Execute the circuit on the qasm backend
    job = execute(circuit, backend, shots = 1024)
    # Grab results from the job
    result = job.result()
    # Returns counts
    counts = result.get_counts(circuit)
    print("\nTotal count are:", counts)
    # Draw the circuit
    print(circuit)
      
# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)
# Add a H gate on qubit 1
circuit.h(0)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])
# Execute
myexe(circuit)

      
# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)
# Add a H gate on qubit 1
circuit.h(1)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])
# Execute
myexe(circuit)

      
# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)
# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])
# Execute
myexe(circuit)

