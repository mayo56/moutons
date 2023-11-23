"""
Fichier principale.
Fichier utilisant la classe Simulation.
"""

from simulation import Simulation

sim = Simulation(
    nombre_moutons=20,
    dimension=50,
    fin_du_monde=100
)
print()
print(sim.simMouton())