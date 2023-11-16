"""
Module de simulation
"""

from mouton import Mouton
from monde import Monde
from random import randint

class Simulation:
    """
    Classe de simulation
    """
    def __init__(self, nombre_moutons, dimension=50, fin_du_monde=1000):

        # Elements physique
        self.nombre_moutons = nombre_moutons
        self.moutons = [
            Mouton(
                (randint(0, dimension - 1), randint(0, dimension - 1)),
                dimension
            ) for _ in range(self.nombre_moutons)
        ]
        self.monde = Monde(30, dimension)

        # Elements temporaires
        self.horloge = 0
        self.fin_du_monde = fin_du_monde
        
        # Elements de stats
        self.resultat_herbe = []
        self.resultat_moutons = []

    def simMouton(self):
        self.horloge += 1
        self.monde.herbePousse()

        all_position = []
        for i in range(len(self.moutons)):
            energie = self.moutons[i].variationEnergie()
            

        # [!] A terminer [!]
