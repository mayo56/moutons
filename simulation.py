"""
Module de simulation
"""

from mouton import Mouton
from monde import Monde
from random import randint
from typing import Dict

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
        self.monde = Monde(2, dimension)

        # Elements temporaires
        self.horloge = 0
        self.fin_du_monde = fin_du_monde
        
        # Elements de stats
        self.resultat_herbe = []
        self.resultat_moutons = []

    def _variation_energie(self, all_position: dict, mon_mouton: Mouton, position: str, index: int, remove_mouton:list) -> int | None:
            energie = None
            pathOfGrass = self.monde.carte[mon_mouton.position[1]][mon_mouton.position[0]] > self.monde.duree_repousse
            # Si la position existe
            if all_position.keys().__contains__(position):
                energie = mon_mouton.variationEnergie(
                    len(all_position[position]) < 1,
                    pathOfGrass
                )            
            # Sinon on la créer
            else:
                all_position[position] = []
                energie = mon_mouton.variationEnergie(
                    True,
                    pathOfGrass
                )
            if pathOfGrass:
                self.monde.herbeMange(mon_mouton.position[0], mon_mouton.position[1])
            # Si l'énergie est None
            if energie == None:
                remove_mouton.append(index)
            else:
                all_position[position].append(mon_mouton)

    def _reproduction(self, all_position: dict):
        reproduction_position = []
        for key, value in all_position.items():
            if len(value) >= 2:
                position = key.split(",")
                reproduction_position.append([int(position[0]), int(position[1])])
        
        for couple in reproduction_position:
            le_couple = []
            n = 0
            for index_mouton in range(len(self.moutons)):
                if n < 2:
                    if self.mouton[index_mouton].position == (couple[0], couple[1]):
                        le_couple.append(index_mouton)
                        n += 1
            
            if self.moutons[le_couple[0]].taux_reproduction == randint(1,100) and self.moutons[le_couple[1]].taux_reproduction == randint(1,100):
                self.moutons.append(Mouton((couple[0], couple[1]), self.monde.dimension))
            

    def simMouton(self):
        while self.horloge < self.fin_du_monde and len(self.moutons) > 0:
            self.horloge += 1
            self.monde.herbePousse()
            print("Temps:", self.horloge)

            all_position = {} # contiendra toutes les positions
                              # {
                              #   "x,y": [Mouton, ...]
                              #   ...
                              # }

            #----+----+----+----+----+----+----+----+----+----#
            #              Variation d'énergie                #
            #----+----+----+----+----+----+----+----+----+----#
            remove_mouton = []
            for i in range(len(self.moutons)):
                # Variation energie
                self._variation_energie(all_position,
                    self.moutons[i], index=i, remove_mouton=remove_mouton,
                    position=str(self.moutons[i].position[0]) + "," + str(self.moutons[i].position[1]),
                )
            remove_mouton.reverse()
            print(remove_mouton)
            for index in remove_mouton:
                self.moutons.pop(index)
            
            print("herbe nombre:", self.monde.nbHerbe())
            print("nombre mouton:", len(self.moutons))

            #----+----+----+----+----+----+----+----+----+----#
            #              Reproduction moutons               #
            #----+----+----+----+----+----+----+----+----+----#
            self._reproduction(all_position)
            
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