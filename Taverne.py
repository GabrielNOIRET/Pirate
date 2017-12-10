# -*- coding: utf-8 -*-
import random
import Navigateur as N
import Equipage as E

class Taverne(object):
    def __init__(self, nomDePirate, prenomDePirate):
        self.listDeNoms = nomDePirate
        self.listDePrenoms = prenomDePirate

    def debaucher(self):
        prixdupirate = random.randint(1, 10)
        force = prixdupirate * 1.5
        nomPrenom = " ".join([self.listDeNoms[random.randint(0, len(self.listDeNoms) - 1)],
                              self.listDePrenoms[random.randint(0, len(self.listDePrenoms) - 1)]])
        return N.Navigateur(nomPrenom, prixdupirate, force=int(force))


def creationListePirateAChoisir(taverne, nbMarins):
    listePirateAChoisir = []
    for i in range(nbMarins):
        pirate = taverne.debaucher()
        listePirateAChoisir.append(pirate)  # On ajoute le nombre de pirates à choisir dans la liste pirate
    return listePirateAChoisir  # On retourne equipage vers listepirate


