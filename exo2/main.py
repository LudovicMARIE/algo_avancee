"""
NightWay - Trouver le chemin le moins risque entre deux adresses.

Le probleme revient a chercher le "plus court chemin" dans un graphe,
ou le poids de chaque liaison est son score de risque. On additionne
les scores le long du chemin et on cherche la somme la plus petite.

On utilise l'algorithme de Dijkstra, qui est concu exactement pour ca.
"""

import csv
import heapq
from collections import defaultdict
from io import StringIO

LIAISONS_CSV = """\
depart,destination,score_risque
Bar Central,Rue Victor Hugo,20
Rue Victor Hugo,Place République,30
Bar Central,Rue des Lilas,50
Rue des Lilas,Place République,10
Place République,Domicile,15
Rue Victor Hugo,Domicile,40
"""


def charger_graphe(donnees_csv, oriente=True):
    """
    Lit les donnees CSV (chaine de caracteres) et construit le graphe.

    Le graphe est un dictionnaire : pour chaque lieu de depart, on garde
    la liste des (destination, score_risque) accessibles.

    oriente=True  -> on ne peut aller que dans le sens depart -> destination.
    oriente=False -> on peut aussi revenir en arriere (utile pour marcher
                     dans une rue dans les deux sens).
    """
    graphe = defaultdict(list)

    lecteur = csv.DictReader(StringIO(donnees_csv))
    for ligne in lecteur:
        depart = ligne["depart"].strip()
        destination = ligne["destination"].strip()
        score = int(ligne["score_risque"])

        graphe[depart].append((destination, score))
        if not oriente:
            graphe[destination].append((depart, score))

    return graphe


def chemin_moins_risque(graphe, depart, arrivee):
    """
    Algorithme de Dijkstra.

    Retourne (risque_total, chemin) ou (None, None) si aucun chemin
    n'existe entre depart et arrivee.
    """
    # risque[lieu] = plus petit risque connu pour atteindre ce lieu depuis le depart
    risque = {depart: 0}
    # predecesseur[lieu] = lieu d'ou l'on vient, pour reconstruire le chemin a la fin
    predecesseur = {depart: None}

    # File de priorite : on explore toujours le lieu au risque cumule le plus faible.
    # Chaque element est un couple (risque_cumule, lieu).
    a_explorer = [(0, depart)]

    while a_explorer:
        risque_courant, lieu = heapq.heappop(a_explorer)

        # Si on sort l'arrivee de la file, on a trouve le meilleur chemin.
        if lieu == arrivee:
            return risque_courant, reconstruire_chemin(predecesseur, arrivee)

        # Si on a deja trouve mieux pour ce lieu entre-temps, on l'ignore.
        if risque_courant > risque.get(lieu, float("inf")):
            continue

        # On regarde tous les voisins accessibles depuis ce lieu.
        for voisin, score in graphe.get(lieu, []):
            nouveau_risque = risque_courant + score
            # A-t-on trouve un chemin moins risque vers ce voisin ?
            if nouveau_risque < risque.get(voisin, float("inf")):
                risque[voisin] = nouveau_risque
                predecesseur[voisin] = lieu
                heapq.heappush(a_explorer, (nouveau_risque, voisin))

    # File vide sans avoir atteint l'arrivee : pas de chemin.
    return None, None


def reconstruire_chemin(predecesseur, arrivee):
    """Remonte les predecesseurs depuis l'arrivee pour retrouver le chemin complet."""
    chemin = []
    lieu = arrivee
    while lieu is not None:
        chemin.append(lieu)
        lieu = predecesseur[lieu]
    chemin.reverse()  # on l'a construit a l'envers (arrivee -> depart)
    return chemin


def main():
    depart = "Bar Central"
    arrivee = "Domicile"

    graphe = charger_graphe(LIAISONS_CSV, oriente=True)
    risque_total, chemin = chemin_moins_risque(graphe, depart, arrivee)

    if chemin is None:
        print(f"Aucun chemin trouve entre '{depart}' et '{arrivee}'.")
    else:
        print("Chemin le moins risque :")
        print("  " + " -> ".join(chemin))
        print(f"Risque total : {risque_total}")


if __name__ == "__main__":
    main()
