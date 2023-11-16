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

    def _variation_energie(self, all_position: dict, mon_mouton: Mouton, str_position: str, index: int) -> int | None:
            energie = None
            # Si la position existe
            if all_position.keys().__contains__(str_position):
                all_position[str_position] += 1
                energie = mon_mouton.variationEnergie(
                    all_position[str_position] < 1,
                    self.monde.carte[mon_mouton.position[1]][mon_mouton.position[0]] > self.monde.duree_repousse
                )            
            # Sinon on la créer
            else:
                all_position[str_position] = 1
                energie = mon_mouton.variationEnergie(
                    True,
                    self.monde.carte[mon_mouton.position[1]][mon_mouton.position[0]] > self.monde.duree_repousse
                )
            # Si l'énergie est None
            if energie == None:
                all_position[str_position] -= 1 # On supprime sa position
                self.moutons.pop(index) # Et son instance dans l'attribut mouton
                 

    def simMouton(self):
        self.horloge += 1
        self.monde.herbePousse()

        all_position = {} # contiendra toutes les positions
                          # {
                          #   "x,y": int
                          #   ...
                          # }

        #----+----+----+----+----+----+----+----+----+----#
        #              Variation d'énergie                #
        #----+----+----+----+----+----+----+----+----+----#
        for i in range(len(self.moutons)):
            mon_mouton = self.moutons[i]
            # str_position: "int,int"
            str_position = str(mon_mouton.position[0]) + "," + str(mon_mouton.position[1])
            # Variation energie
            self._variation_energie(all_position, mon_mouton, str_position, i)

        #----+----+----+----+----+----+----+----+----+----#
        #              Reproduction moutons               #
        #----+----+----+----+----+----+----+----+----+----#
        # ...
        
        #----+----+----+----+----+----+----+----+----+----#
        #                   Deplaceent                    #
        #----+----+----+----+----+----+----+----+----+----#
        for mouton in self.moutons:
            mouton.deplacement()

        #----+----+----+----+----+----+----+----+----+----#
        #             Sauvegarde des données              #
        #----+----+----+----+----+----+----+----+----+----#
        # ...
        
            
            
        

lol = Simulation(20, 50, 10000)
lol.simMouton()