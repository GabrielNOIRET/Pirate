# -*- coding: utf-8 -*-
import random
import Navigateur as N
import Equipage as E

nomDePirate = ["Bonny", "Jack", "Teach", "Drake", "Morgan", "Nau", "Read"]
prenomDePirate = ["Anne", "Calico", "Edward", "Francis", "Henry", "Jean", "Mary"]

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


taverneAPirate = Taverne(nomDePirate, prenomDePirate)
listePirate = creationListePirateAChoisir(taverneAPirate, 3)

for i in listePirate:
    print i.nom, i.argent, i.force

equipage = E.Equipage(N.Navigateur("Blabla",10,10))
