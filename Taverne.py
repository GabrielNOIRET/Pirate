# -*- coding: utf-8 -*-
# Importation des bibliothèques fichiers
import random
import Navigateur as N
import Equipage as E


# Création de la classe Taverne
class Taverne(object):
    # Définition du constructeur
    def __init__(self, nomDePirate, prenomDePirate):
        self.listDeNoms = nomDePirate
        self.listDePrenoms = prenomDePirate

    # Fonction permettant de créer des pirates en leur associant un nom prénom, une force et un prix
    def debaucher(self):
        prixdupirate = random.randint(50, 300) #Attribution d'un prix aléatoire
        force = prixdupirate * 1.5 #Attribution d'une force en fonction du prix
        # Création du nomPrenom du prirate avec un jointure d'un prenom et d'un nom choisis aléatoirements dans deux listes
        nomPrenom = " ".join([self.listDePrenoms[random.randint(0, len(self.listDePrenoms) - 1)],
                              self.listDeNoms[random.randint(0, len(self.listDeNoms) - 1)]])
        return N.Navigateur(nomPrenom, prixdupirate, force=int(force))


# Fonction permettant de récupérer les pirates créés pour les implémanter dans la liste des pirates à choisir
def creationListePirateAChoisir(taverne, nbMarins):
    listePirateAChoisir = [] # -initialisation de la liste
    for i in range(nbMarins):
        pirate = taverne.debaucher()
        listePirateAChoisir.append(pirate)  # On ajoute le nombre de pirates à choisir dans la liste pirate
    return listePirateAChoisir


