"""
Module contenant la classe des moutons.
"""

from random import randint


# Variable aléatoire pour le déplacement
# 1 : Nord (Haut)
# 2 : Nord Ouest
# 3 : Ouest (Gauche)
# 4 : Nord Est
# 5 : Sud (Bas)
# 6 : Sud Ouest
# 7 : Est (Droite)
# 8 : Sud Est
_DEPLACEMENT_MATRICE = {
    # [x,y]
    "1": [1,0],
    "2": [1,-1],
    "3": [0,-1],
    "4": [1,1],
    "5": [-1,0],
    "6": [-1,-1],
    "7": [0,1],
    "8": [-1,1],
}


class Mouton:
    """
    Classe du mouton.
    """

    def __init__(self, dimension=50):
        """
        Constructeur
        """
        self.dimenson = dimension  # On met les params dans self
        self.gain_nourriture = 4
        self.energie = randint(1, 2) * self.gain_nourriture
        self.taux_reproduction = 4
        self.position = (49, 49) # (x,y)

    def variationEnergie(self, first:bool, ):
        """
        mdr
        """
        pass

    def deplacement(self):
        """
        Fonction permettant au mouton de se mouvoir sur le monde.
        """
        # constante ayant les valeurs de déplacement du mouton
        DIRECTION_DEPLACEMENT = _DEPLACEMENT_MATRICE[str(randint(1, 8))]
        # (x,y)
        new_positions = (
            self.position[0] + DIRECTION_DEPLACEMENT[0], # x
            self.position[1] + DIRECTION_DEPLACEMENT[1]  # y
        )

        # Sortie Nord -> Sud
        if (new_positions[0] + 1) % (self.dimenson - 1) == 0:
            new_positions = (self.dimenson - 1, new_positions[1])

        # Sortie Ouest -> Est
        if (new_positions[1] + 1) % (self.dimenson - 1) == 0:
            new_positions = (new_positions[0], self.dimenson - 1)

        # Sortie Sud -> Nord
        if new_positions[0] % (self.dimenson) == 0:
            new_positions = (0, new_positions[0])

        # Sortie Est -> Ouest
        if new_positions[1] % (self.dimenson) == 0:
            new_positions = (new_positions[0], 0)
        
        # On attribut les nouvelles valeurs
        self.position = new_positions

mon_mouton = Mouton(50)
mon_mouton.deplacement()
