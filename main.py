"""
Ce fichier contient les instructions de démarrage
de la smulation avec les moutons.
"""

from simulation import Simulation

sim:Simulation = Simulation(
    nombre_moutons=50,
    dimension=50,
    fin_du_monde=100
)
print("[[Moutons], [Herbe]]")
print(sim.simMouton())