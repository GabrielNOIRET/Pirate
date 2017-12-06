# -*- coding: utf-8 -*-
class Equipage(object):
    def __init__(self, listeMarins):
        self.listeMarins = listeMarins

    def ajoutMarin(self, marinChoisi):
        self.listeMarins.append(marinChoisi)

    def afficheMarins(self):  # Fonction qui affiche les noms des Marins dans l'équipage
        self.nbMarin = 0
        for i in Equipage.listeMarins:
            self.nbMarin += 1
            print "L'équipage est composé de", self.nbMarin, "pirates : "
            print "-", i.nom


