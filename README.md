# bloch-sphere-visualizer
A Qiskit-based visualization tool that demonstrates how common single-qubit quantum gates transform states on the Bloch sphere.

## Project Overview

The Bloch sphere is a geometric representation of a single qubit. By visualizing quantum states as vectors on a sphere, quantum gate operations can be interpreted as rotations in three-dimensional space.

This project uses Qiskit to generate quantum states and Matplotlib to create a custom Bloch sphere visualization from scratch.

---

## Theory

### State Mapping to the Bloch Sphere

A general single-qubit pure state can be written as:

|ψ⟩ = cos(θ/2)|0⟩ + e^(iφ)sin(θ/2)|1⟩

where:

* θ is the polar angle
* φ is the azimuthal angle

Every pure quantum state corresponds to a point on the surface of the Bloch sphere.

The Bloch coordinates are calculated from the statevector amplitudes α and β:

x = 2Re(ᾱβ)

y = 2Im(ᾱβ)

z = |α|² − |β|²

These coordinates determine the position of the quantum state on the sphere.

### Geometric Representation of the Axes

#### Z-Axis (Computational Basis)

* +Z corresponds to |0⟩
* -Z corresponds to |1⟩

#### X-Axis (Superposition Basis)

* +X corresponds to |+⟩ = (|0⟩ + |1⟩)/√2
* -X corresponds to |-⟩ = (|0⟩ - |1⟩)/√2

#### Y-Axis (Phase Basis)

* +Y corresponds to |i⟩ = (|0⟩ + i|1⟩)/√2
* -Y corresponds to |-i⟩ = (|0⟩ - i|1⟩)/√2

### Pure and Mixed States

Pure states represent complete knowledge of a quantum system and always lie on the surface of the Bloch sphere.

Mixed states represent statistical uncertainty or decoherence and lie inside the sphere.

The centre of the Bloch sphere corresponds to a maximally mixed state where there is an equal probability of measuring |0⟩ or |1⟩ and all phase information has been lost.

---

## Quantum Gates as Rotations

Quantum gates can be interpreted as rotations of the Bloch vector.

### Pauli-X Gate

Performs a π (180°) rotation around the X-axis.

### Pauli-Y Gate

Performs a π (180°) rotation around the Y-axis.

### Pauli-Z Gate

Performs a π (180°) rotation around the Z-axis.

### Hadamard Gate

Creates a superposition state:

|0⟩ → (|0⟩ + |1⟩)/√2

This moves the Bloch vector from the positive Z-axis to the positive X-axis.

### Phase Gates

The S gate applies a π/2 rotation around the Z-axis.

The T gate applies a π/4 rotation around the Z-axis.

---

## Implementation

The program:

1. Creates a single-qubit quantum circuit using Qiskit.
2. Applies a selected quantum gate.
3. Generates the resulting statevector.
4. Converts the statevector into Bloch coordinates.
5. Constructs a custom three-dimensional Bloch sphere using Matplotlib.
6. Displays the resulting quantum state as a vector on the sphere.

### Supported Gates

* X
* Y
* Z
* H
* S
* T


