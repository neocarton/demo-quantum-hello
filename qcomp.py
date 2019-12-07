# Reference:
# https://github.com/Qiskit/qiskit-community-tutorials/blob/master/hello_world/hello_zero.ipynb
# https://delapuente.github.io/qiskit-textbook

from qiskit import (IBMQ, providers, Aer, execute)
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def fetchBackend() :
    # IBM Q backend
    IBMQ.load_accounts()
    backend = providers.ibmq.least_busy(IBMQ.backends(simulator = False))
    print("Using the least busy device:", backend.name())
    return backend

def qexec(circuit, backend = None, shots = 1000) :
    if backend is None :
        backend = defaultBackend
    # Execute the circuit on the qasm backend
    job = execute(circuit, backend, shots = shots)
    # Grab results from the job
    result = job.result()
    # Print
    print_result(circuit, result)
    # Draw
    draw_result(circuit, result)

def print_result(circuit, result) :
    counts = result.get_counts(circuit)
    statevec = result.get_statevector()
    print(circuit)
    print("Counts :", counts)
    print("State vectors:", statevec)

def draw_result(circuit, result) :
    counts = result.get_counts(circuit)
    statevec = result.get_statevector()
    circuit.draw(output = "mpl")
    plot_histogram(counts)
    plot_bloch_multivector(statevec)

# List IBMQ backends
# provider = IBMQ.get_provider(hub='ibm-q')
# provider.backends()

# List simulators
# unitary_simulator
# statevector_simulator
# qasm_simulator
# print(Aer.backends())

defaultBackend = Aer.get_backend("statevector_simulator")
print("Default backend:", defaultBackend.name())
