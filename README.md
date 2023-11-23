# Un monde de mouton et de loups...

## Objectif
On veut modéliser le fonctionnement d'un écosystème, avec de l'herbe, des moutons et des loups: les moutons mangent l'herbe, les loups mangent les moutons.

Cette simulation est discrète: tous les "tours de jeu", les moutons ainsi que les loups se déplacent, mangent éventuellement, meurt parfois, et l'herbe pousse.

L'interêt est d'observer l'évolution de la "population " de chaque protagoniste, l'herbe, les moutons et les loups.

*Il est possible de visualiser les courbes de population. Le code et recopié en fin de document, il est très court.*

## 1. Les moutons et l'herbe
Classe moutons
--------------
### Principe:
Cette classe est la carte sur laquelle évoluent les moutons.

ELle a pour attribut (entre autres) un tableau de carré `carte` de dimension 50 x 50 (ou plus), qui représente une prairie.

Chaque case du tableau représente une zonne sur laquelle pousse de l'herbe.

Ce tableau contient des entiers qui codent la présence ou pas d'herbe:
- Si la valeur de l'entier est inférieur à l'entier `duree_repousse` il n'y a pas d'herbe
- Si la valeur est supérieure, il y en a, et l'herbe repousse à une vitesse donnée (entier `duree_repousse` entre 1 et 100, on peut mettre 30).

Le coefficient dans une case du tableau est réinitialisé à 0 lorsqu'un moutons "occupe" la case et mange l'herbe.

À chaque "battement d'horloge" modélisant l'évolution du temps, on augmente la valeur ddans chaque case de 1 pour modéliser la pousse de l'herbe (vous verrez la gestion du temps dans la classe Simulation).

### Attributs
- `dimension`
- `duree_repousse`
- `carte`
### Méthodes
- Le constructeur peut avoir un paramètre facultatif `dimension = 50`
- `herbePousse()`
- `herbeMangee(x,y)`, où `x` et `y` sont les coordonnées d'une case de la catye
- `nbHerbe()` qui renvoie le nombre de carrés de la carte qui contiennent de l'herbe.

On pourra initialiser les coefficients des cases de la carte à 50% de carré herbus, et pour ceux qui n'otn pas d'herbe on initialisera le coeficient à 0 et `duree_repousse` aléatoirement.

Classe Mouton
-----
### Attributs
- Le constructeur a comme paramètres dimension, la diemnsion du monde, afin de placer correctement les moutons
- `gain_energie` le gain d'énergie apporté par la consommation d'un carré d'herbe (on peut mettre 4)
- `position` couple d'entier indiquant les coordonnées de la case de la carte occupée par le mouton
- `energie` entier positif (ou nul). Quand l'énergie du mouton est à zéro, il meurt et l'objet est supprimée. Sera initialisé entre 1 et 2 x `gain_nourriture`
- `taux_reproduction` entier compris entre 1 et 100 (on peut mettre 4). Ce taux représente le pourcentage de chance qu'un mouton se reproduise (par parthénogénèse ici)

### Methodes
- `variationEnergie()` diminue de 1 l'énergie du mouton s'il n'est pas sur un carré d'hebr, sinon augmente `energie`` de `gain_nourriture`. Remarque: si plusieurs moutons sont sur la même case herbue, seul le premier bénéficie du gain d'énergie. Réfléchissez bien aux paramètres de cette méthode.
- `deplacement()` le mouton se déplace aléatoirement dans une des huit cases adjacentes de celle où il se trouve.

Est plus facile de considérer les monde comme dans les jeux vidéo: soritr par le haut de la carte renvoie en bas etc, on utilise alors l'opératuer modula (%).

On peut accpeter le fait que le mouton ne se déplace pas à tous les coups, cela simplifie la programmation.

## 2. La simulation
Un classe Simulation, comme son nom l'indique, gèrera la simulation. La mettre dans un autre fichier. On y importe les calsses Monde et Mouton: On utilisera les classes Monde et Mouton de la même manière que l'on utilise une bibliothèque.

### Attributs
- `nombre_moutons` entier
- `horloge` entier initialisé à 0 au début de la simulation
- `fin_du_monde` entier donnant le "temps" maximum de la simulation
- `moutons` liste d'objets de type Mouton (il y en a `nombre_moutons`)
- `monde` une instance de la classe Monde
- `resulats_herbe` liste construite petit à petit, dont chaque élément est le nombre de carrés d'herbe à chaque "battement d'horloge"

### Methodes
Une seule méthode, `simMouton()` gère la simulation en créant une boucle qui remplira plusieurs fonctions les une après les autres:
- Augmente `horloge` de 1 à chaque appel
- Fait pousser l'herbe
- appelle variationEnergie() pour chaque mouton. Si l'énergie d'un mouton est nulle, l'instance de celui-ci est supprimée (suppression de l'élément correspondant dans la liste des moutons)
- Fait se reproduire les moutons. Un nouveua mouton apparît sur la même case que son parent, avec un "pourcentage de naissance" donnée par `taux_reproduction`. Un mouton qui se reproduit a son énergie divisé par 2. On peut mettre la naissance dans une des 9 cases du voisinage du mouton (modulo la dimension de la carte), y compris la case où est le mouton reproducteur.
- Fait se déplacer les moutons.
- Sauvegarde dans `resultats_herbe` et `resultats_moutons` les nombres de carrés herbus et de moutons du tour.

On peut arrêter la simulation s'il n'y a plus de moutons ou s'il y en a plus qu'un nombre fixé (qu'on rajoutera en attribut). Dans ce dernier cas, les moutons ont conquis le monde... On l'arrête dans tous les cas lorsque l'horloge sonne la fin du monde.

La methode renvoie les deux listes de résultat `resultats_herbe` et `resultats_moutons`, `resultats_loups` si ;les loups ont été reajoutés...

Pour les tests, mettre `fin_du_monde` à 10. Réfléchissez aussi si à ce qui peut dse passer en ce qui concerne le nombre de moutons d'une génération à la suivante. Les tests peuvent être très longs dès que l'on dépasse 100 "battement" d'horloge suivant votre ordinateur.

Il est fortement conseillé d'utiliser le code proposé pour vidualiser les résultats.

```py
# REMPLACEZ si nécessaire le nom du fichier à emporter (simulation_ecologie)
# REMPLACEZ si necessaire le nom de la méthode "sim.simMouton" pour la simulationn

import numpy as np
import matplotlib.pyplot as plt
import simulation_ecologie as simul

# Pour un test sans les loups, supprimez Y3
sim = simul.Simulation()

# Y1, Y2 = sim.simMouton()
Y1, Y2, Y3 = sim.simMouton()

# print("Herbe:", Y1)
# print("Moutons:", Y2)
# print("Loups:", Y3)

for i in range (len(Y1)):
    Y1[i] = Y[i]/4

X = np.linspace(0, len(Y1), len(Y1), endpoint=True)

plt.plot(X, Y1, 'g')
plt.plot(X, Y2, 'b')
plt.plot(X, Y3, 'k')

plt.plot(X, Y1, color="green", linewidth=2.5, linstyle="-", label="Herbe/4")
plt.plot(X, Y1, color="blue", linewidth=2.5, linstyle="-", label="Moutons")
plt.plot(X, Y1, color="black", linewidth=2.5, linstyle="-", label="Loups")

plt.legend(loc='upper left', frameon=True)
plt.show()
```

## 3. On rajoute les loups
Les loups "fonctionnent" comme les moutons, sauf qu'ils ne mangent pas d'herbe mais plutôt des moutons... Un loup ne mange qu'un seul mouton par tour.

On peut leur mettre un taux de reproduction de 5, et un gain sur la nourriture de 19. Si le gain est trop petit les loups meurent tous, s'il est trop grand les loups se multiplient trop, et avec les données de naissances la croissance devient exponentielles.

Il est logique de mettre dau moins deux fois moins de loups que de moutons. Avec ces données et les précédentes, on obtient un système qui se stabilise.

Il est intéressant de trouver des valeurs initiales qui donnent un systèle pseudo-périodique (des sortes de sinusoïdes décallés) , ou bien des systèmes chaotiques.