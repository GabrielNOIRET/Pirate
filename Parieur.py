# coding=utf-8
# Importation des bibliothèques fichiers
import random

# multiplicateurs pour calculer les gains, l'ordre correspond à celui des cartes de 1 au roi
multiplicateurs_plus_haut = (0, 1.1, 1.1, 1.1, 1.3, 1.5, 1.7, 2.1, 2.6, 3.5, 5.3, 10.7, 0)
# multiplicateurs inverse, on fait une copie de multiplicateurs_plus_haut que l'on inverse et reconvertit en tuple
multiplicateurs_plus_faible = list(multiplicateurs_plus_haut)
multiplicateurs_plus_faible.reverse()
multiplicateurs_plus_faible = tuple(multiplicateurs_plus_faible)

class Parieur:
    # Définition du constructeur
    def __init__(self):
        self.cartes = []
        self.genereCartes()

    # Fonction qui génère les 52 cartes
    def genereCartes(self):
        familles = ('Coeur', 'Carreau', 'Trefle', 'Pique')
        for famille in familles:
            for valeur in range(1, 11, 1):
                self.cartes.append({'valeur': valeur, 'desc': str(valeur) + ' de ' + famille})
            self.cartes.append({'valeur': 11, 'desc': 'Valet de ' + famille})
            self.cartes.append({'valeur': 12, 'desc': 'Reine de ' + famille})
            self.cartes.append({'valeur': 13, 'desc': 'Roi de ' + famille})
        random.shuffle(self.cartes)

    # Fonction pour jouer 5 tours avec le parieur, retourne les gains
    def joue(self):
        print "- - - - - - - - - - - - - - - - - - - - - -"
        print "- - - - - PARIEUR - - - - - -"
        print "- - - - - - - - - - - - - - - - - - - - - -"
        print "Je suis le Parieur et on va jouer a 'Plus Haut / Plus Bas'."
        print "J\'ai un paquet de {0} cartes\n".format(str(len(self.cartes)))
        gain = 0
        nombreDeTours = 5
        for i in range(0, nombreDeTours, 1):
            print "- - - - - - - - - - - - - - - - - -"
            print "Tour {0}/{1}".format(str(i+1), str(nombreDeTours)), "\t------\tGain: {0} pieces".format(str(gain))
            print "- - - - - - - - - - - - - - - - - -\n"
            gain += self.joueTour()
            if i < nombreDeTours - 1:
                raw_input("\nOn continue...(appuie sur une touche)\n")

        print "Fin du jeu !"
        return gain

    # Fonction pour jouer 1 tour avec le parieur en utilisant le packet de carte, retourne le gain
    def joueTour(self):
        # on prend la derniere carte du paquet (correspond au dessus du paquet)
        carteVisible = self.cartes[-1]

        # tant que la derniere carte vaut 1 ou Roi, on la met sous le paquet (on ne peut pas parier avec ces valeurs)
        while carteVisible['valeur'] == 1 or carteVisible['valeur'] == 13:
            self.cartes.insert(0, self.cartes.pop())
            carteVisible = self.cartes[-1]

        # maintenant, on est sur que carteVisible est ok (pas de 1 ou Roi)
        # on peut regarder la carte en dessus du paquet qui n'est pas retournée
        carteDessusPaquet = self.cartes[-2]

        # on calcule les variables de résultat
        estPlusBas = carteVisible['valeur'] > carteDessusPaquet['valeur']
        estPlusHaut = carteVisible['valeur'] < carteDessusPaquet['valeur']
        estEgale = carteVisible['valeur'] == carteDessusPaquet['valeur']
        gain = 0

        # on trouve les multiplicateurs en fonction de la carte visible pour les choix plus haut et plus bas
        multiplicateurPlusBas = multiplicateurs_plus_faible[carteVisible['valeur'] - 1]
        multiplicateurPlusHaut = multiplicateurs_plus_haut[carteVisible['valeur'] - 1]

        print "Carte visible  -->  " + carteVisible['desc'] + "\n"
        message = "La carte suivante sera plus \n"
        message += "1. Faible ? (+{0} pieces)\n".format(str(int(10 * multiplicateurPlusBas)))
        message += "2. Forte ? (+{0} pieces)\n".format(str(int(10 * multiplicateurPlusHaut)))
        choix = raw_input(message)
        while choix not in ("1", "2"):
            choix = raw_input("Choix incorrect, tapez 1 ou 2 :")

        print "Je retourne la carte du dessus  -->  " + carteDessusPaquet['desc'] + "\n"

        if estEgale:
            print 'match nul !!'

        elif choix == "1":
            if estPlusBas:
                print "Tu gagnes!"
                gain = 1 * multiplicateurPlusBas
            else:
                print "Tu perds!"
                gain = -1 * multiplicateurPlusHaut

        else:
            if estPlusHaut:
                print "Tu gagnes!"
                gain = 1 * multiplicateurPlusHaut
            else:
                print "Tu perds!"
                gain = -1 * multiplicateurPlusBas

        # important de remettre la carte visible en dessous du paquet
        self.cartes.insert(0, self.cartes.pop())

        # retourne le gain multiplié par 10
        return int(gain * 10)