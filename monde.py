"""
Ce module contient la classe du monde où évoluent les moutons.
"""

class Monde:
    """
    Cette classe est la carte sur laquelle évoluent les moutons.
    """
    def __init__(self, duree_repousse:int, dimension=50) -> None:
        # Vérification des types
        assert isinstance(duree_repousse, int), ValueError("Le paramètre \"duree_repousse\" doit etre un integer.")
        assert isinstance(dimension, int), ValueError("Le parametre \"dimension\" doit etre un integer.")

        # Vérification des valeurs
        assert duree_repousse > 1 or duree_repousse < 100, ValueError("\"duree_repousse\" doit etre compris entre 1 et 100.")
        assert dimension >= 50, ValueError("\"duree_repousse\" doit etre superieur ou egal a 50.")

        # Attribut duree_repousse
        self.duree_repousse = duree_repousse

        # Creation du monde. Useage: carte[y][x]
        self.carte = []
        for y in range(dimension): # y de la carte
            self.carte.append([])
            for _ in range(dimension): # x de la carte
                self.carte[y].append(0)
    
    def herbePousse(self) -> None:
        """
        Fonction permettant de faire pousser l'herbe sur la carte.
        Ajoute 1 à chaque case de la carte.
        """
        for indice_y, y in enumerate(self.carte):
            for indice_x, _ in enumerate(y):
                self.carte[indice_y][indice_x] += 1
    
    def herbeMange(self, x:int, y:int) -> None:
        """
        Fonction permettant de supprimer l'herbe mangée (par un mouton).
        Met la case d'herbe mangé à 0. (A la position x;y)
        """
        self.carte[y][x] = 0

    def nbHerbe(self) -> int:
        """
        Fonction permettant de savoir le nombre de case d'herbe disponible sur la carte.
        Renvoie le nombre de case d'herbe disponible de type integer.
        """
        nombre_herbe = 0
        for _, y in enumerate(self.carte):
            for _, x in enumerate(y):
                if x >= self.duree_repousse:
                    nombre_herbe += 1
        return nombre_herbe