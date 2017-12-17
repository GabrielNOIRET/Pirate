# coding=utf-8
# Importation des bibliothèques fichiers
import random
import Navigateur as N

nomsDePirate = ("Bonny", "Jack", "Teach", "Collaart", "Morgan", "Nau", "Read", "Riskinner", "Oxenham", "Compaan",
               "Cavendish", "Mainwaring", "Essex", "Morris", "Braziliano", "Sawkins", "Anstis", "Culliford",
               "Henríquez", "Neumann")

prenomsDePirate = ("William", "Calico", "Edward", "John", "Henry", "Jean", "Mary", "James", "Isaac", "Jan", "Vincenzo",
                  "Jacquotte", "Cornelius", "George", "Thomas", "Lars", "Miguel", "Edward", "Christopher", "Mary",
                  "Flora")


# Fonction permettant de créer des pirates en leur associant un nom prénom, une force et un prix
def creePirate():
    # Attribution d'un prix aléatoire
    prixDuPirate = random.randint(50, 300)

    # Attribution d'une force en fonction du prix
    forceDuPirate = int(prixDuPirate * 1.5)

    # Création du nomPrenom du pirate avec un prénom et un nom choisi aléatoirement dans les tuples de noms et prénoms
    nomPrenom = random.choice(prenomsDePirate) + " " + random.choice(nomsDePirate)

    return N.Navigateur(nomPrenom, prixDuPirate, forceDuPirate)


# Création de la classe Taverne
class Taverne(object):
    # Définition du constructeur
    def __init__(self):
        self.pirates = []
        self.generePirates()

    # Fonction qui génère des pirates dans la taverne
    def generePirates(self):
        # Boucle pour créer 10 pirates
        for i in range(10):
            pirate = creePirate()

            # Ajout du pirate dans la liste pirates
            self.pirates.append(pirate)


# # Fonction permettant de récupérer les pirates créés pour les implémanter dans la liste des pirates à choisir
# def creationListePirateAChoisir(taverne, nbMarins):
#     listePirateAChoisir = [] # -initialisation de la liste
#     for i in range(nbMarins):
#         pirate = taverne.debaucher()
#         listePirateAChoisir.append(pirate)  # On ajoute le nombre de pirates à choisir dans la liste pirate
#     return listePirateAChoisir


