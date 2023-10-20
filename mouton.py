"""
Module contenant la classe des moutons.
"""

from random import randint

class Mouton:
    """
    Classe du mouton.
    """
    def __init__(self, dimension):
        """
        Constructeur
        """
        self.dimenson = dimension # On met les params dans self
        self.gain_nourriture = 4
        self.energie = (randint(1,2) * self.gain_nourriture)
        self.taux_reproduction = 4

    def variationEnergie(self):
        """
        mdr
        """
        pass
    
    def deplacement(self):
        """
        mdr
        """
        pass
    
