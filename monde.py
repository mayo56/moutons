"""
Ce module contient la classe Monde pour la simulation avec les moutons.

# Methodes

herbePousse()
-------------
    Fait pousser de l'herbe sur chaque case de la carte.
    (La case devient herbus quand le nombre dans la case est supperieur ou égal à la durre_repousse)

herbeMange(x, y)
----------------
    Permet à un mouton de manger une case herbus sur la carte à l'emplacement (x, y).

nbHerbe()
---------
    Renvoi le nombre de case herbus sur la carte.
    (Principalement conçut pour des résultats ou stats).
"""

class Monde:
    """
    Classe du monde. Permet de générer un monde sur une dimension demander.
    Le monde contient de l'herbe qui peut pousser.
    """
    def __init__(self, duree_repousse, dimension=50):
        """
        Génère un monde en deux dimensions de forme carré (dimension x dimension) et
        d'avoir de l'herbe sur chaque case poussant tout les duree_repouse temps.

        Paramètres:
        - `durree_repousse` int -> durée au bout du quel l'herbe a poussé
        - `dimension` int -> dimension du monde [Prédéfinit à 50]

        Utilisation:
        ```py
        mon_monde = Monde(10, 50)
        mon_monde = Monde(10)
        ```
        """
        # Vérification des types
        assert isinstance(duree_repousse, int), TypeError("Le paramètre \"duree_repousse\" doit etre un integer.")
        assert isinstance(dimension, int), TypeError("Le parametre \"dimension\" doit etre un integer.")

        # Vérification des valeurs
        assert duree_repousse > 1 or duree_repousse < 100, ValueError("\"duree_repousse\" doit etre compris entre 1 et 100.")
        assert dimension >= 50, ValueError("\"duree_repousse\" doit etre superieur ou egal a 50.")

        # Attribut 
        self.duree_repousse = duree_repousse
        self.dimension = dimension

        # Creation du monde. Useage: carte[y][x]
        self.carte = []
        for y in range(dimension): # y de la carte
            self.carte.append([])
            for _ in range(dimension): # x de la carte
                self.carte[y].append(0)
    
    def herbePousse(self) -> None:
        """
        * Ne retourne rien.
        * Ne prend aucune paramètres.

        Methode permettant de faire pousser l'herbe sur chacune des cases
        de la carte.

        Exemple:
        ```py
        monde = Monde(10)
        monde.herbePousse()
        ```
        """
        for indice_y, y in enumerate(self.carte): # Boucle sur les y
            for indice_x, _ in enumerate(y): # boucle sur les x
                self.carte[indice_y][indice_x] += 1 # Ajout de l'herbe (+1)
    
    def herbeMange(self, x, y):
        """
        * Ne retourne rien.
        
        Paramètres:
        - `x` int -> les coordonnées en x
        - `y` int -> les coordonnées en y

        Methode permettant de manger un carré d'herbe
        aux coordonnées ( x ; y )

        Exemple:
        ```py
        monde = Monde(10)
        monde.herbeMange(10,20)
        ```
        """
        # Vérification de type
        assert isinstance(x, int) and isinstance(y, int), TypeError("Les paramètres \"x\" et \"y\" doivent être des integers.")

        # Met à zéro le carré demandé
        self.carte[y][x] = 0

    def nbHerbe(self):
        """
        * Retourne le nombre de carré d'herbe herbus. (int)
        * Ne prend aucun paramètres.

        Methode permettant de récuperer le nombre de carré d'herbe herbus
        sur la carte.

        Exemple:
        ```py
        monde = Monde(10)
        print(monde.nbHerbe())
        # >>> 20
        ```
        """
        nombre_herbe = 0
        for _, y in enumerate(self.carte): # Boucle sur les y
            for _, x in enumerate(y): # Boucle sur les x
                if x >= self.duree_repousse:
                    nombre_herbe += 1 # On récupère s'il est herbus
        return nombre_herbe