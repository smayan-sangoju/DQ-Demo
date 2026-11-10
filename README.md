# Project 1: How fast does noise break a Bell state?

**Team:** [Partner A], [Partner B]
**Track:** Algorithms
**Chapter:** Do Quantum @ UVA, Fall 2026

## Our hypothesis

Raising the error rate on the CNOT gate lowers the share of correct
Bell-state results (00 or 11).

| | |
|---|---|
| What we change | The error rate on the CNOT gate |
| What we measure | The share of shots that come back 00 or 11 |
| What stays fixed | The circuit and the number of shots |

## How we tested it

A two-qubit Bell-state circuit on the Qiskit Aer simulator, run with a
depolarizing noise model at five error rates.

```
pip install qiskit qiskit-aer
python code/bell_noise.py
```

## What we found

| CNOT error rate | Correct results |
|---|---|
| 0% | 100.0% |
| 1% | 99.4% |
| 5% | 97.1% |
| 10% | 94.5% |
| 20% | 89.7% |

The share of correct results drops as the error rate goes up, which
supports the hypothesis.

## What is in this repo

- `code/` scripts and notebooks
- `notes/` papers we read and what we took from them
- `slides/` our talk

## What we want to do next

[One or two sentences on the question you want to research next, and why.]
