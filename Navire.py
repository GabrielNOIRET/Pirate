# coding=utf-8
import Equipage as E
import Carte


# Création de la classe Navire
class Navire(object):
    # Définition du constructeur
    def __init__(self, nom, argent, capitaine):
        self.nom = nom
        self.argent = argent
        self.capitaine = capitaine
        # self.portDepart = pd
        self.equipage = E.Equipage([])

    # Fonction qui initialise la position du bateau (dans le port de Rabat)
    def initPosition(self):
        Carte.positionneBateau(self.portDepart)
        self.portActuel = self.portDepart

    # Fonction qui met à jour la nouvelle position saisie par l'utilisateur
    def actualisePosition(self, position):
        Carte.positionneBateau(position)
        self.portActuel = position

    def depense(self, montant):
        argentAvantDepense = self.argent
        self.argent -= montant
        message = "Le " + self.nom + " dépense " + str(montant) + " pièces !"
        message += "\t(Butin précédent: " + str(argentAvantDepense) + ", Butin actuel: " + str(self.argent) + ")"
        print message

    def gagne(self, montant):
        argentAvantGain = self.argent
        self.argent += montant
        message = "Le " + self.nom + " gagne " + str(montant) + " pieces !"
        message += "\t(Butin précédent: " + str(argentAvantGain) + ", Butin actuel: " + str(self.argent) + ")"
        print message

    # Fonction qui propose et met à jour l'emplacement du bateau et de la dernière route
    def bougePosition(self):


        # destinationsPossible = Carte.trouveDestinationsProches()
        #
        # message = "Quel est le prochain port de destination ? :"
        #
        # for index, destination in enumerate(destinationsPossible):
        #     message += "\n" + str(index + 1) + ". " + destination["port"] + "\t(" + str(destination["cout"]) + " pieces)"
        #
        # choix = raw_input(message)
        # while choix not in ("1", "2", "3"):
        #     choix = raw_input("Choix incorrect, tapez 1, 2 ou 3 :")
        #
        # destinationChoisie = destinationsPossible[int(choix)-1]
        #
        # print destinationChoisie

        # supprimerRoutes()






        '''
        saisie = False
        while saisie == False:
            portEscale = raw_input("Quel est le prochain port de destination ? :")
            portEscale = portEscale.replace(' ', '')
            Jeu.action(self)
            # print "On va bouger le bateau"
            if portEscale in ("1", "2", "3"):
                creationRoute(nomdest[int(portEscale) - 1])
                coutdest = int(coutdest[int(int(portEscale) - 1)] * 10)
                portEscale = nomdest[int(int(portEscale) - 1)]

                self.actualisePosition(portEscale)

                # lieuArrive = portEscale
                # if lieuArrive == 'Istanbul':
                #   Jeu.arriveeIstanbul()

                saisie = True
            # Essaie de saisie des noms de destinations en lettres
            # elif portEscale in nomdest:
            #   creationRoute(portEscale)
            #  for i in range(len(nomdest)):
            #     if portEscale == nomdest[i]:
            #        print int(coutdest[i])*10
            #       coutdest = int(coutdest[i])*10
            # self.actualisePosition(portEscale)

            # saisie = True

            else:
                propositionDestination()
                print "Ressaisie la destination, tape une destination entre 1 2 ou 3"
                saisie = False

        # def coutdestination(coutdest):
        #   self.argent -= int(coutdest)
        #  print "Vous êtes arrivé à", portEscale, ", il vous reste,",self.argent, "pieces d'or"
        # coutdestination(coutdest)
        '''