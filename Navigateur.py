# -*- coding: utf-8 -*-
import random

class Navigateur(object):
    def __init__(self, nom, argent, force):
        self.nom = nom
        self.tete = 1
        self.nbYeux = 2
        self.nbBras = 2
        self.nbJambes = 2
        self.prix = argent
        self.force = force
        self.vivant = True

    def blesse(self):

         if 1 < random.randint(0, 10):
             self.tete = 0

         else:

             if self.nbJambes > 0:
                 self.nbJambes = self.nbJambes - 1

             elif self.nbBras > 0:
                 self.nbBras = self.nbBras - 1

             elif self.nbYeux > 0:
                 self.nbYeux = self.nbYeux - 1


         if self.tete == 0 or self.nbYeux == 0:
             self.vivant = False
