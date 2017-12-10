# -*- coding: utf-8 -*-
class Equipage(object):
    def __init__(self, listeMarins):
        self.listeMarins = listeMarins

    def ajoutMarin(self, marinChoisi):
        self.listeMarins.append(marinChoisi)

    def afficheMarins(self):  # Fonction qui affiche les noms des Marins dans l'équipage
        print "L'équipage est composé de", len(self.listeMarins), "pirates : "
        for marin in self.listeMarins:
            print "-", marin.nom




