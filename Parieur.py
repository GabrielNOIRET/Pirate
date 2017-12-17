# coding=utf-8
# Importation des bibliothèques fichiers
import random


multiplicateurs = (0, 1.1, 1.1, 1.1, 1.3, 1.5, 1.7, 2.1, 2.6, 3.5, 5.3, 10.7, 0)
reversed_multiplicateurs = list(multiplicateurs)
reversed_multiplicateurs.reverse()
reversed_multiplicateurs=tuple(reversed_multiplicateurs)

class Parieur:

    def __init__(self):
        self.cartes = []
        self.genereCartes()

    def genereCartes(self):
        familles = ('Coeur', 'Carreau', 'Trefle', 'Pique')
        for famille in familles:
            for valeur in range(1, 11, 1):
                self.cartes.append({'valeur': valeur, 'desc': str(valeur) + ' de ' + famille})
            self.cartes.append({'valeur': 11, 'desc': 'Valet de ' + famille})
            self.cartes.append({'valeur': 12, 'desc': 'Reine de ' + famille})
            self.cartes.append({'valeur': 13, 'desc': 'Roi de ' + famille})
        random.shuffle(self.cartes)

    def play(self):
        print "- - - - - - - - - - - - - - - - - - - - - -"
        print "- - - - - PARIEUR TOUR - - - - - -"
        print "- - - - - - - - - - - - - - - - - - - - - -"
        print "Je suis le Parieur et on va jouer a 'Plus Haut / Plus Bas'."
        print "J\'ai un paquet de {0} cartes\n".format(str(len(self.cartes)))
        gain = 0
        maxRound = 5
        for i in range(0, maxRound, 1):
            print "- - - - - - - - - - - - - - - - - -"
            print "Tour {0}/{1}".format(str(i), str(maxRound)), "\t------\tGain: {0} pieces".format(str(gain))
            print "- - - - - - - - - - - - - - - - - -\n"
            gain += self.playRound()
            if i < maxRound - 1:
                raw_input("\nOn continue...\n")

        return gain

    def playRound(self):
        # prend la derniere carte du paquet (correspond au dessus du paquet)
        carteVisible = self.cartes[-1]

        # tant que la derniere carte vaut 1 ou Roi, on la met sous le paquet
        while carteVisible['valeur'] == 1 or carteVisible['valeur'] == 13:
            self.cartes.insert(0, self.cartes.pop())
            carteVisible = self.cartes[-1]

        # maintenant, on est sur que carteVisible est ok (pas de 1 ou Roi)
        # on peut regarder la carte en dessus du paquet
        carteDessusPaquet = self.cartes[-2]

        plusBas = carteVisible['valeur'] > carteDessusPaquet['valeur']
        plusHaut = carteVisible['valeur'] < carteDessusPaquet['valeur']
        egale = carteVisible['valeur'] == carteDessusPaquet['valeur']
        gain = 0

        multiplicateurPlusBas = reversed_multiplicateurs[carteVisible['valeur']-1]
        multiplicateurPlusHaut = multiplicateurs[carteVisible['valeur']-1]

        print "Carte visible  -->  " + carteVisible['desc'] + "\n"
        message = "La carte suivante sera plus \n"
        message += "1. Faible ? (x {0})\n".format(str(multiplicateurPlusBas))
        message += "2. Forte ? (x {0})\n".format(str(multiplicateurPlusHaut))
        choix = raw_input(message)
        while choix not in ("1", "2"):
            choix = raw_input("Choix incorrect, tapez 1 ou 2 :")

        print "Je retourne la carte du dessus  -->  " + carteDessusPaquet['desc'] + "\n"

        if egale:
            print 'match nul !!'

        elif choix == "1":
            if plusBas:
                print "Tu gagnes!"
                gain = 1 * multiplicateurPlusBas
            else:
                print "Tu perds!"
                gain = -1 * multiplicateurPlusHaut

        else:
            if plusHaut:
                print "Tu gagnes!"
                gain = 1 * multiplicateurPlusHaut
            else:
                print "Tu perds!"
                gain = -1 * multiplicateurPlusBas

        # important de remettre la carte visible en dessous du paquet
        self.cartes.insert(0, self.cartes.pop())

        return int(gain * 10)