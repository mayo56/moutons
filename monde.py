"""
Ce module contient la classe du monde où évoluent les moutons.
"""

class Monde:
    """
    Cette classe est la carte sur laquelle évoluent les moutons.
    """
    def __init__(self, duree_repousse:int, dimension=50):
        self.__init_value_verification(duree_repousse, dimension)

        # Attribut duree_repousse
        self.duree_repousse = duree_repousse
        
        # Creation du monde
        self.carte = []
        for y in range(dimension): # y de la carte
            self.carte.append([])
            for _ in range(dimension): # x de la carte
                self.carte[y].append(0)
    
    def __init_value_verification(self, duree_repousse:int, dimension:int):
        """
        Fonction permettant de verifier les parametres de la classe.
        | NOM | TYPE | VALEUR | 
        | :---- | :----: | -----: |
        | duree_repousse | int | Entre 1 et 100 |
        | dimension | int | Superieur ou egal a 50 |

        """
        # Vérification des types
        if not isinstance(duree_repousse, int):
            raise ValueError("Le paramètre \"duree_repousse\" doit etre un integer.")
        elif not isinstance(dimension, int):
            raise ValueError("Le parametre \"dimension\" doit etre un integer.")
        
        # Vérification des valeurs
        if duree_repousse < 1 or duree_repousse > 100:
            raise ValueError("\"duree_repousse\" doit etre compris entre 1 et 100.")
        if dimension < 50:
            raise ValueError("\"duree_repousse\" doit etre superieur ou egal a 50.")
    
    def herbePousse(self):
        pass
    
    def herbeMange(self, x:int, y:int):
        """
        Manger de l'herbe à l'endroit x;y
        """
        pass

    def nbHerbe(self):
        """
        Nombre de carré d'herbe sur la carte
        """
        pass

    
mon_monde = Monde(52,50)