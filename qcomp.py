# Reference:
# https://github.com/Qiskit/qiskit-community-tutorials/blob/master/hello_world/hello_zero.ipynb

from qiskit import (IBMQ, providers, Aer, execute)

def fetchBackend() :
    # IBM Q backend
    IBMQ.load_accounts()
    backend = providers.ibmq.least_busy(IBMQ.backends(simulator = False))
    print("Using the least busy device:", backend.name())
    return backend

def getSimulator() :
    # Aer's qasm_simulator
    backend = Aer.get_backend('qasm_simulator')
    print("Using:", backend.name())
    return backend

def qexec(circuit, backend = None, shots = 1000) :
    if backend is None :
        backend = defaultBackend
    # Execute the circuit on the qasm backend
    job = execute(circuit, backend, shots = shots)
    # Grab results from the job
    result = job.result()
    # Returns counts
    counts = result.get_counts(circuit)
    print("\nTotal count are:", counts)
    # Draw the circuit
    print(circuit)

defaultBackend = getSimulator()
