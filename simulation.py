"""
Module de simulation
"""

from mouton import Mouton
from monde import Monde
from random import randint

class Simulation:
    """
    Classe de simulation. Permet de générer une simulation contenant un monde et des moutons.
    Il permet de retourner des resultat sur la vie des moutons dans le monde.
    """
    def __init__(self, nombre_moutons:int, dimension:int=50, fin_du_monde:int=10) -> None:
        """
        Génère une simulation contenant un monde de dimension (dimension x dimension) et
        contenant le nombre de mouton demande. La simulation de passe en batement d'horloge
        et se termine quand le nombre de batemant atteint la fin du monde.

        Paramètres:
        - `nombre_moutons` int -> nombre de moutons pour la simulation
        - `dimension` int -> dimension du monde [Prédéfinit à 50]
        - `fin_du_monde` int -> nombre de batement d'horloge, duree de la simulation [Prédéfinit à 10]

        Utilisation:
        ```py
        sim = Simulation(10, 50, 20)
        sim = Simulation(10, dimension=50)
        sim = Simulation(10, fin_du_monde=20)
        sim = Simulation(10)
        ```
        """
        # Verification des types
        assert isinstance(nombre_moutons, int), TypeError("Le paramètre \"nombre_moutons\" doit être un integer.")
        assert isinstance(dimension, int), TypeError("Le paramètre \"dimension\" doit être un integer.")
        assert isinstance(fin_du_monde, int), TypeError("Le paramètre \"fin_du_monde\" doit être un integer.")

        # Vérification valeur
        assert nombre_moutons > 0, ValueError("Le paramètre \"nombre_moutons\" doit être plus grand que 0.")
        assert dimension > 0, ValueError("Le paramètre \"dimension\" doit être plus grand que 0.")
        assert fin_du_monde > 0, ValueError("Le paramètre \"fin_du_monde\" doit être plus grand que 0.")


        # Elements physique
        self.nombre_moutons:int = nombre_moutons
        self.moutons:list[Mouton] = [
            Mouton(
                (randint(0, dimension - 1), randint(0, dimension - 1)), # Position aléatoire
                dimension
            ) for _ in range(self.nombre_moutons)
        ]
        self.monde:Monde = Monde(50, dimension)

        # Elements lie au temp
        self.horloge:int = 0
        self.fin_du_monde:int = fin_du_monde
        
        # Elements de stats
        self.resultat_herbe:list = []
        self.resultat_moutons:list = []

    def _variation_energie(self, all_position: dict[str, list[int]]) -> list[int]:
        """
        * Methode privée.
        * Retourne la liste des moutons qui sont à court d'energie (`list[int]`).

        Paramètres:
        - `all_position` dict[str, list[int]] -> contient les index des moutons présent en position (x,y) [key: position, value: liste des index]
        
        Methode permetant de faire varier l'energie de tous les moutons et renvoyer les index de chaque moutons
        n'ayant plus d'energie.
        """
        remove_mouton:list[int] = []

        for index in range(self.nombre_moutons):
            mon_mouton:Mouton = self.moutons[index] # Notre mouton
            position:str = str(mon_mouton.position[0]) + "," + str(mon_mouton.position[1]) # Sa position en str
            energie:None | int = None # Son energie
            pathOfGrass:bool = self.monde.carte[mon_mouton.position[1]][mon_mouton.position[0]] > self.monde.duree_repousse # Est-il sur un carre d'herbe herbus

            # Si la position existe
            if all_position.keys().__contains__(position):
                energie = mon_mouton.variationEnergie(
                    len(all_position[position]) < 1, # S'il est seul: reçoit de l'energie
                    pathOfGrass
                )
            # Sinon on la créer
            else:
                all_position[position] = []
                energie = mon_mouton.variationEnergie(True, pathOfGrass)
            # On mange le carré d'herbe s'il existe
            if pathOfGrass:
                self.monde.herbeMange(mon_mouton.position[0], mon_mouton.position[1])

            # Si l'énergie est None
            if energie == None:
                remove_mouton.append(index) # On l'ajoute à la liste des moutons à enlever
            else:
                all_position[position].append(index) # On l'ajoute à la liste des moutons
        return remove_mouton
        

    def _reproduction(self, all_position: dict[str, list[Mouton]]) -> None:
        """
        * Methode privée.
        * Ne retourne rien.

        Paramètres:
        - `all_position` dict[str, list[int]] -> contient les index des moutons présent en position (x,y) [key: position, value: liste des index]
        
        Methode permettant de faire reproduire les moutons s'ils sont deux sur une même case de la carte.
        Ne faire reproduire que les deux premier moutons.
        """
        # [
        #     [x, y, [index_1, index_2]]
        # ]
        reproduction_position: list[list[int, int, list[int, int]]] = []

        for key, value in all_position.items():
            if len(value) >= 2:
                position:list[str, str] = key.split(",") # On coupe la position "x,y" -> ["x", "y"]
                reproduction_position.append([int(position[0]), int(position[1]), value[0:2]]) # Ajout [ x, y, [index_1, index_2] ]

        for couple in reproduction_position: # Boucle sur les positions
            le_couple:list[int] = couple[2]
            # /!\
            # /!\ [À Modif car pas bon] /!\
            # /!\           |
            # /!\           | Ce qui suit
            # /!\           v
            if self.moutons[le_couple[0]].taux_reproduction == randint(1,100) and self.moutons[le_couple[1]].taux_reproduction == randint(1,100):
                self.moutons.append(Mouton((couple[0], couple[1]), self.monde.dimension))
            

    def simMouton(self) -> list[list[int], list[int]]:
        """
        * Retourne les listes de resulatat des moutons et des herbes (`list[list[int], list[int]]`)
        * Ne prend aucun paramètres.

        Methode permettant de demarrer la simulation.

        Exemple:
        ```py
        sim = Simulation(10)
        sim.simMouton()
        """
        while self.horloge < self.fin_du_monde and self.nombre_moutons > 0:
            self.horloge += 1
            self.monde.herbePousse()

            # all_position: contiendra toutes les positions des moutons
            # {
            #   "x,y": [int, ...]
            #   ...
            # }
            all_position:dict[str, list[int]] = {}

            #----+----+----+----+----+----+----+----+----+----#
            #              Variation d'énergie                #
            #----+----+----+----+----+----+----+----+----+----#
            remove_mouton = self._variation_energie(all_position)
            remove_mouton.reverse()
            for index in remove_mouton: # Supprime les moutons morts
                self.moutons.pop(index)
                self.nombre_moutons -= 1

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
            self.resultat_herbe.append(self.monde.nbHerbe())
            self.resultat_moutons.append(self.nombre_moutons)

        return [self.resultat_moutons, self.resultat_herbe]