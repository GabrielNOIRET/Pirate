# -*- coding: utf-8 -*-
# Importation des bibliothèques fichiers
import random


# Création de la classe Equipage
class Equipage(object):
    # Définition du constructeur
    def __init__(self, listeMarins):
        self.listeMarins = listeMarins

    # Fonction qui rajoute à la liste de la listeMarins le marin choisi par l'utilisateur
    def ajoutMarin(self, marinChoisi):
        self.listeMarins.append(marinChoisi)

    # Fonction qui enlève un marin de la liste au hasard et le retourne
    def enleveMarinAleatoirement(self):
        marinEnleve = random.choice(self.listeMarins)
        self.listeMarins.remove(marinEnleve)
        return marinEnleve

    # Fonction qui affiche les noms des Marins dans l'équipage
    def afficheMarins(self):
        print "L'équipage est composé de", len(self.listeMarins), "pirates : "
        for marin in self.listeMarins:
            print "-", marin.nom

    # Fonction qui calcule la force totale des marins
    def calculForce(self):
        forceTotale = 0
        for marin in self.listeMarins:
            forceTotale += marin.force
        return forceTotale

    # Fonction qui actualise la liste des marins aprés un évènement (combat ou tempête)
    def endommage(self):

        listeMarinsVivants = []
        for marin in self.listeMarins:
            marin.blesse()

            # Condition si les marins sont toujours vivants
            if marin.vivant == True:
                listeMarinsVivants.append(marin)

        # Remplacement de la liste des marins avec la liste des marins toujours vivants

        affichePerte = raw_input("Vous avez subit des pertes. Voulez vous voir ? (y/n)")
        if affichePerte == "y":
            print "- Nombre de marins avant: " + str(len(self.listeMarins))
            print "- Nombre de marins après: " + str(len(listeMarinsVivants)) + "\n"
            for marin in self.listeMarins:
                marin.afficheBlesse()
                print "...."
            print "------"
        self.listeMarins = listeMarinsVivants















