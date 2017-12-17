# coding=utf-8
# Importation des bibliothèques fichiers
import random

from Navigateur import Navigateur
from Parieur import Parieur

# Tuples de noms de navigateurs
nomsDePirate = ("Bonny", "Jack", "Teach", "Collaart", "Morgan", "Nau", "Read", "Riskinner", "Oxenham", "Compaan",
               "Cavendish", "Mainwaring", "Essex", "Morris", "Braziliano", "Sawkins", "Anstis", "Culliford",
               "Henríquez", "Neumann")

# Tuples de prénoms de navigateurs
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

    return Navigateur(nomPrenom, prixDuPirate, forceDuPirate)


# Création de la classe Taverne
class Taverne(object):
    # Définition du constructeur
    def __init__(self):
        self.pirates = []
        self.generePirates()
        self.parieur = Parieur()

    # Fonction qui génère des pirates dans la taverne
    def generePirates(self):
        # Boucle pour créer 10 pirates
        for i in range(10):
            pirate = creePirate()

            # Ajout du pirate dans la liste pirates
            self.pirates.append(pirate)

    # Fonction qui controle la visite de la taverne, initialise les attributs par rapport au visiteur
    def visite(self, argentDisponible):
        self.depenseVisiteur = 0
        self.argentVisiteur = argentDisponible
        self.panierMarins = []
        self.finVisite = False
        print "Bienvenue dans la taverne. Ici, vous pouvez acheter des marins ou jouer avec le Parieur"

        while not self.finVisite:
            self.proposeVisiteActions()

        print "Vous quittez la taverne! Bon vent!"

    # Fonction qui imprime les actions possibles, recupère le choix et appelle la fonction correspondante
    def proposeVisiteActions(self):
        print "1. Acheter des Marins"
        print "2. Jouer aved le Parieur"
        print "3. Sortir de la taverne"
        choixAction = raw_input("Que voulez-vous faire?\n")
        while choixAction not in ("1", "2", "3"):
            choixAction = raw_input("Choix incorrect, tapez 1, 2 ou 3 :")

        if choixAction == "1":
            self.achatMarins()

        elif choixAction == "2":
            self.jeuAvecParieur()

        # Sinon, le choix est 3 et finVisite devient True
        else:
            self.finVisite = True

    # Fonction qui permet d'acheter des marins
    def achatMarins(self):
        print "Voici les pirates disponibles : "
        # la variable choixPossibles est une liste qui contient ce que l'utilisateur peut entrer, vide au début
        choixPossibles = []
        for index, pirate in enumerate(self.pirates):
            numeroChoix = str(index + 1)
            print numeroChoix + ".", pirate.nom + "\t\t(prix: " + str(pirate.prix) + " force: " + str(pirate.force) + ")"
            # on ajoute le numéro dans les choix
            choixPossibles.append(numeroChoix)

        # on ajoute 'q' dans les choix
        choixPossibles.append('q')

        choixPirate = raw_input("\nQuel pirate voulez-vous ? ('q' pour arrêter)")
        while choixPirate not in choixPossibles:
            choixPirate = raw_input("Choix incorrect!")

        # si le choix n'est pas de quitter
        if choixPirate != 'q':
            # on calcule l'index du pirate
            indexPirate = int(choixPirate) - 1
            # on retrouve le pirate dans la liste
            pirateChoisi = self.pirates[indexPirate]

            # on regarde si on peut acheter le pirate, on effectue l'achat que si le visiteur a assez d'argent
            if pirateChoisi.prix > self.argentVisiteur:
                print "Ce pirate est trop cher pour vous !"

            else:
                print "Vous achetez : " + pirateChoisi.nom
                # on retire le pirate de la liste des pirates de la taverne
                self.pirates.remove(pirateChoisi)
                # on ajoute le pirate dans le panier
                self.panierMarins.append(pirateChoisi)
                # on recalcule l'argent restant et la dépense
                self.argentVisiteur -= pirateChoisi.prix
                self.depenseVisiteur += pirateChoisi.prix

            print "Vous avez acheté "+str(len(self.panierMarins)) + " pirate(s)!"
            print "Il vous reste " + str(self.argentVisiteur) + " pièces!"

            # on propose d'acheter un autre pirate
            choix = raw_input("Voulez-vous acheter un autre pirate ? (y/n)")
            while choix not in ['y', 'n']:
                choix = raw_input("Choix incorrect!")

            # on rappelle cette fonction si le visiteur veut acheter un autre pirate
            if choix == 'y':
                self.achatMarins()

    # Fonction qui permet de jouer avec le Parieur de la taverne
    def jeuAvecParieur(self):
        # on récupère le resultat de la partie
        resultat = self.parieur.joue()
        # on recalcule l'argent restant et la dépense
        self.argentVisiteur += resultat
        self.depenseVisiteur -= resultat

        if resultat < 0:
            print "Le Parieur a été plus fort, vous perdez " + str(resultat) + " pièces."
            print "Il vous reste " + str(self.argentVisiteur) + " pièces."

        elif resultat > 0:
            print "Vous avez battu Le Parieur, vous gagnez " + str(resultat) + " pièces."
            print "Vous avez maintenant " + str(self.argentVisiteur) + " pièces."

        else:
            print "Vous avez joué, ni gagné, ni perdu."
