"""
Module contenant la classe des moutons.
"""

from random import randint

# Constante contenant tous les déplacements selon l'orientation
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
    "1": (1,0),
    "2": (1,-1),
    "3": (0,-1),
    "4": (1,1),
    "5": (-1,0),
    "6": (-1,-1),
    "7": (0,1),
    "8": (-1,1),
}

class Mouton:
    """
    Classe des Mouton. Permet de générer un mouton ayant une position sur une carte.
    Il peut se déplacer et varier son énergie.
    """
    def __init__(self, position:tuple[int, int], dimension:int=50):
        """
        Génère un mouton sur une carte de dimension (dimension x dimension)
        à une position donnée (x ; y).

        Paramètres:
        - `position` tuple (x,y) -> coordonnée du mouton sur la carte.
        - `dimension` int -> dimension du monde [Prédéfinit à 50]

        Utilisation:
        ```py
        mon_mouton = Mouton((10,20), 50)
        mon_mouton = Mouton((10,20))
        ```
        """
        # Vérifications
        assert isinstance(position, tuple), TypeError("Position doit être un tuple.")
        assert isinstance(dimension, int), TypeError("Le paramètre \"dimension\" doit être un integer.")
        assert len(position) == 2, ValueError("Position doit contenir deux coordonnées: (x, y)")
        assert isinstance(position[0], int) and isinstance(position[1], int), TypeError("Position doit contenir des integers. (int, int)")
        assert dimension > 0, ValueError("Le paramaètre \"dimension\" doit être plus grand que 0.")

        self.dimenson:int = dimension  # On met les params dans self
        self.gain_nourriture:int = 4
        self.energie:int = randint(1, 2) * self.gain_nourriture
        self.taux_reproduction:int = randint(1,100)
        self.position:tuple[int, int] = position # (x,y) 

    def variationEnergie(self, first:bool, onPatchOfGrass: bool) -> int | None:
        """
        * Retourn l'energie du mouton (`int`) ou `None`.

        Paramètres:
        - `first` bool -> si le mouton est le premier sur la case d'herbe
        - `onPatchOfGrass` bool -> si le carre d'herbe est herbus

        Methode qui permet d'ajouter de l'energie au mouton s'il
        se trouve sur une case d'herbe herbus et s'il est le premier.
        Sinon, il enlève de l'energie.

        Exemple:
        ```py
        mouton = Mouton((x,y))
        mouton.variationEnergie(True, True) # Ajoute de l'energie
        mouton.variationEnergie(True, False) # Enlève de l'energie
        mouton.variationEnergie(False, True) # Enlève de l'energie
        mouton.variationEnergie(False, False) # Enlève de l'energie
        """
        # Vérifications typages
        assert isinstance(first, bool), TypeError("Le paramètres \"first\" doit être un booleen")
        assert isinstance(onPatchOfGrass, bool), TypeError("Le paramètres \"onPatchOfGrass\" doit être un booleen")

        if onPatchOfGrass: # Si sur une case herbus
            if first: # Si premier
                self.energie += self.gain_nourriture # Ajoute de l'energie
                return self.energie
        self.energie -= 1 # Retire de l'energie
        if self.energie == 0: # Si mort du mouton
            return None
        return self.energie

        

    def deplacement(self) -> None:
        """
        * Ne retourne rien.
        * Ne prends aucun paramètres.

        Methode permettant au mouton de se déplacer sur les 8 cases
        autour de lui. Il se déplace seulement d'une seule case.

        Exemple:
        ```py
        mouton = Mouton((x,y))
        mouton.deplacement()
        ```
        """
        # constante ayant les valeurs de déplacement du mouton
        DIRECTION_DEPLACEMENT:list[int, int] = _DEPLACEMENT_MATRICE[str(randint(1, 8))]
        # (x,y)
        new_positions:tuple[int, int] = (
            self.position[0] + DIRECTION_DEPLACEMENT[0], # x
            self.position[1] + DIRECTION_DEPLACEMENT[1]  # y
        )

        # Si un mouton sort des limites de la carte
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