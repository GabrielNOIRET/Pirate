# -*- coding: utf-8 -*-
import random

class Equipage(object):
    def __init__(self, listeMarins):
        self.listeMarins = listeMarins

    def ajoutMarin(self, marinChoisi):
        self.listeMarins.append(marinChoisi)

    def afficheMarins(self):  # Fonction qui affiche les noms des Marins dans l'équipage
        print "L'équipage est composé de", len(self.listeMarins), "pirates : "
        for marin in self.listeMarins:
            print "-", marin.nom

    def calculForce(self):
        forceTotale = 0
        for marin in self.listeMarins:
            forceTotale += marin.force
        return forceTotale

    def endommage(self):
        listeMarinsVivants = []
        for marin in self.listeMarins:
            marin.blesse()
            if marin.vivant == True:
                listeMarinsVivants.append(marin)

        self.listeMarins = listeMarinsVivants













