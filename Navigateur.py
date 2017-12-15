# -*- coding: utf-8 -*-
# Importation des bibliothèques fichiers
import random


# Création de la classe Navigateur
class Navigateur(object):
    # Définition du constructeur
    def __init__(self, nom, argent, force):
        self.nom = nom
        self.tete = 1
        self.nbYeux = 2
        self.nbBras = 2
        self.nbJambes = 2
        self.prix = argent
        self.force = force
        self.vivant = True

    # Création de la fonction blesse.
    # Fonction permettant de définir l'ordre de perte de menbres des pirates pour les combats
    def blesse(self):

        # Condition sur un entier aléatoire qui va ou non supprimer la tête
        if random.randint(0, 10) < 2:
            self.tete = 0

        # Condition sur l'ordre de pertes des membres
        else:

            if self.nbJambes > 0:
                self.nbJambes = self.nbJambes - 1

            elif self.nbBras > 0:
                self.nbBras = self.nbBras - 1

            elif self.nbYeux > 0:
                self.nbYeux = self.nbYeux - 1

        # Si un marin n'a plus de tête ou plus ses deux yeux alors il meurt
        if self.tete == 0 or self.nbYeux == 0:
            self.vivant = False

        print self.nom
        print "Tete: " + str(self.tete)
        print "Jambes: " + str(self.nbJambes)
        print "Bras: " + str(self.nbBras)
        print "Yeux: " + str(self.nbYeux)
        print "Vivant: " + str(self.vivant)

