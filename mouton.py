from random import *
class Mouton:
    """
    lol
    """
    def __init__(self,dimension,variationEnergie,position,energie,taux_reproduction):
        """
        Constructeur
        """
        self.dimension = dimension
        self.variationEnergie = variationEnergie # gain d'energie apporte par la consommation d'un carre d'herbe
        self.position = position # couple d'entiers indiquant les coordonnees de la case de la carte occupee par le mouton
        self.energie = energie # entier positif(ou nul), quand l'energie d'un mouton = 0 il meurt et l'objet est supprime
        self.taux_reproduction = taux_reproduction # entier compris entre 1 et 100, % de chance qu'un mouton se reproduise

    def __init_value_verification(self,dimension,variationEnergie,position,energie,taux_reproduction):
        pass

    def variation_energie(self):
        """
        mdr
        """
        pass
    
    def deplacement(self):
        """
        mdr
        """
        pass
    
