from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

import numpy as np
import matplotlib.pyplot as plt


# Converts a single-qubit statevector into Bloch sphere coordinates.
def state_to_bloch(state):

    alpha = state.data[0]
    beta = state.data[1]

    x = 2 * np.real(np.conjugate(alpha) * beta)
    y = 2 * np.imag(np.conjugate(alpha) * beta)
    z = np.abs(alpha) ** 2 - np.abs(beta) ** 2

    return x, y, z


# Creates a 3D Bloch sphere and plots a quantum state vector.
def plot_bloch_sphere(x, y, z, title="Bloch Sphere"):

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Sphere
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(xs, ys, zs, alpha=0.1)

    # Axes
    ax.plot([-1, 1], [0, 0], [0, 0])
    ax.plot([0, 0], [-1, 1], [0, 0])
    ax.plot([0, 0], [0, 0], [-1, 1])

    # State vector
    ax.quiver(0, 0, 0, x, y, z, linewidth=3)

    ax.text(1.1, 0, 0, "+X")
    ax.text(-1.2, 0, 0, "-X")

    ax.text(0, 1.1, 0, "+Y")
    ax.text(0, -1.2, 0, "-Y")

    ax.text(0, 0, 1.1, "|0⟩")
    ax.text(0, 0, -1.2, "|1⟩")

    ax.set_title(title)

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    plt.show()


# Applies a quantum gate to a qubit initially prepared in |0⟩ and visualizes the resulting state on the Bloch sphere.
def visualize_gate(gate):

    qc = QuantumCircuit(1)

    if gate == "X":
        qc.x(0)

    elif gate == "Y":
        qc.y(0)

    elif gate == "Z":
        qc.z(0)

    elif gate == "H":
        qc.h(0)

    elif gate == "S":
        qc.s(0)

    elif gate == "T":
        qc.t(0)

    else:
        raise ValueError("Unsupported gate")

    state = Statevector.from_instruction(qc)

    x, y, z = state_to_bloch(state)

    print(f"\n{gate} Gate")
    print(f"Bloch Coordinates: ({x:.3f}, {y:.3f}, {z:.3f})")

    plot_bloch_sphere(x, y, z, title=f"{gate} Gate")


if __name__ == "__main__":

    visualize_gate("X")
    visualize_gate("Y")
    visualize_gate("Z")
    visualize_gate("H")
    visualize_gate("S")
    visualize_gate("T")
