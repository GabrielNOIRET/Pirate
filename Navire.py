# coding=utf-8
import Carte

# Création de la classe Navire
from Equipage import Equipage

# Création de la classe Navigateur
class Navire(object):
    # Définition du constructeur
    def __init__(self, nom, argent, capitaine):
        self.nom = nom
        self.argent = argent
        self.capitaine = capitaine
        # self.portDepart = pd
        self.equipage = Equipage([])

    # Fonction qui initialise la position du bateau (dans le port de Rabat)
    def initPosition(self, portDepart):
        print "Le navire commence à " + portDepart
        self.actualisePosition(portDepart)

    # Fonction qui met à jour la nouvelle position saisie par l'utilisateur
    def actualisePosition(self, position):
        Carte.positionneBateau(position)
        self.portActuel = position

    # Fonction qui dépense l'argent (dépensé lorsque que l'on saisie une destination ou lorsque l'on va dans une taverne)
    def depense(self, montant):
        argentAvantDepense = self.argent
        self.argent -= montant
        message = "Le " + self.nom + " dépense " + str(montant) + " pièces !"
        message += "\t(Butin précédent: " + str(argentAvantDepense) + ", Butin actuel: " + str(self.argent) + ")"
        print message

    # Fonction qui ajoute de l'argent (gagné lorsque l'on gagne un combat ou au carte dans la taverne)
    def gagne(self, montant):
        argentAvantGain = self.argent
        self.argent += montant
        message = "Le " + self.nom + " gagne " + str(montant) + " pièces !"
        message += "\t(Butin précédent: " + str(argentAvantGain) + ", Butin actuel: " + str(self.argent) + ")"
        print message
