"""Project 1 demo: how fast does noise break a Bell state?

Hypothesis: raising the two-qubit gate error rate lowers the share of
correct Bell-state results (00 or 11).

What we change:  the error rate on the CNOT gate
What we measure: the share of shots that come back 00 or 11
What stays fixed: the circuit and the number of shots

Run with:  python code/bell_noise.py
Needs:     pip install qiskit qiskit-aer
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error

SHOTS = 4000
ERROR_RATES = [0.0, 0.01, 0.05, 0.10, 0.20, 0.30]


def bell_circuit():
    """Build the two-gate circuit that makes a Bell state."""
    circuit = QuantumCircuit(2)
    circuit.h(0)      # put qubit 0 in superposition
    circuit.cx(0, 1)  # entangle qubit 1 with qubit 0
    circuit.measure_all()
    return circuit


def correct_share(error_rate):
    """Run the circuit with noise and return the share of 00 and 11 results."""
    noise = NoiseModel()
    if error_rate > 0:
        noise.add_all_qubit_quantum_error(depolarizing_error(error_rate, 2), ["cx"])

    simulator = AerSimulator(noise_model=noise)
    circuit = transpile(bell_circuit(), simulator)
    counts = simulator.run(circuit, shots=SHOTS, seed_simulator=7).result().get_counts()

    good = counts.get("00", 0) + counts.get("11", 0)
    return good / SHOTS


if __name__ == "__main__":
    print("CNOT error rate -> share of correct results")
    for rate in ERROR_RATES:
        print(f"  {rate:>5.0%}  ->  {correct_share(rate):.1%}")
