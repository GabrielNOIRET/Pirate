# coding=utf-8
# Importation des bibliothèques fichiers
import Navire as B
import Equipage as E
import Taverne as T
import Navigateur as N
import random


# Fonction qui aléatoirement choisi un évènement (Combat, Sirène, Tempête, Pas d'évènement)
def action(leNavire):
    numAction = random.randint(0, 10)
    numAction = 0

    if numAction < 3:
        combat(leNavire)

    elif numAction == 3:
        print "Sirène"

    elif numAction == 4:
        print "Tempête"



# Fonction qui fait un combat
def combat(unNavire):
    print " "
    print "Nous voici en route mais malheureusement sur notre chemin se trouve un pavillon ennemi "
    print "--------- Combat ! ---------"
    print "Vous disposez de",unNavire.argent, "pièces d'or"

    # obtention de la force totale de notre navire
    forceNavire = unNavire.equipage.calculForce()
    # obtention aléatoire de la force du bateau ennemie par rapport à notre force
    forceEnnemi = ((random.randint(-100, 100)) * forceNavire / 100) + forceNavire
    # Calcule de la chance de victoire en fonction de notre force et de la force ennemie
    # (La chance de victoire repose le hasard d'avoir plus ou moins de la chance de victoire, il s'agit d'une sorte de pari)
    chanceEnnemi = (100 * forceEnnemi) / (forceNavire + forceEnnemi)
    print "La force de notre ennemi est de", forceEnnemi, ". Notre force est de", forceNavire
    # Choix de l'utilisateur de combattre ou non
    choixCombat = raw_input("Voulez-vous combattre ? (y/n)")
    if choixCombat == "y":
        if random.randint(0,100) > chanceEnnemi:
            butin = random.randint(10, 200)
            print "Gagné!, vous remportez", butin,"pièces d'or. Il vous reste", unNavire.argent, "pièces d'or"
            print "Aprés un combat acharné, continuons notre périble..."
            #TODO ajouter argent gagné
            unNavire.argent += butin
            #TODO Couper des membres!
        else:
            print "Perdu..."
            #nbMarins = len(unNavire.equipage.listeMarins)
            #TODO Faire appel fonction blesse
            #blesse(unNavire.equipage.listeMarins[random.randint(0,nbMarins)])



    else:
        print "Froussard, on continue la route !"






if __name__ == "__main__":

    #listAccident = ["bras", "jambe", "yeux"]
    nomDePirate = ["Bonny", "Jack", "Teach", "Collaart", "Morgan", "Nau", "Read", "Riskinner", "Oxenham", "Compaan", "Cavendish", "Mainwaring", "Essex", "Morris", "Braziliano", "Sawkins", "Anstis", "Culliford", "Henríquez", "Neumann"]
    prenomDePirate = ["William", "Calico", "Edward", "John", "Henry", "Jean", "Mary", "James", "Isaac", "Jan", "Vincenzo", "Jacquotte", "Cornelius", "George", "Thomas", "Lars", "Miguel", "Edward", "Christopher", "Mary", "Flora"]


    print "Bien le bonjour à toi jeune Corsaire, nous avons besoin de toi pour récupérer les diamants pour se faire tu vas devoir composer un équipage et te rendre à Istambul !"
    nomCapitaine = raw_input("Commence par choisir le nom de ton capitaine : ")
    capitaine = N.Navigateur(nomCapitaine, 10, 12)
    debutListeMarins = [capitaine]
    nautilus = B.Navire("Nautilus", 1000, "Rabat", debutListeMarins)
    #equipage = E.Equipage(N.Navigateur("Blabla", 10, 10))


    #taverneAPirate = T.Taverne(nomDePirate, prenomDePirate)
    #listePirate = T.creationListePirateAChoisir(taverneAPirate, 3)



    capitaine = N.Navigateur(nomCapitaine, 10, 12)

    nautilus.equipage.afficheMarins()
    #print "Voici les pirates disponibles : "
    #for index, pirate in enumerate(listePirate):
     #   print index+1, ".", pirate.nom, "Cout: ", pirate.argent, "Force: ", pirate.force


    def visiterTaverne ():
        print "Vous disposez de ",nautilus.argent,"pièces d'or"
        taverneAPirate = T.Taverne(nomDePirate, prenomDePirate)
        listePirate = T.creationListePirateAChoisir(taverneAPirate, 3)

        print "Voici les pirates disponibles : "
        for index, pirate in enumerate(listePirate):
            print index + 1, "-", pirate.nom, "(prix: ", pirate.prix, " force: ", pirate.force,")"

        def selectionAchatPirate():
            choixPirate = raw_input("Quel pirate voulez-vous ?(Tapez q pour sortir de la taverne)")
            if choixPirate in ("1", "2", "3"):

                pirateChoisi = listePirate[int(choixPirate) - 1]
                if nautilus.argent - pirateChoisi.prix < 0:
                    print "Ce pirate est trop cher pour vous !"
                    selectionAchatPirate()
                else:
                    nautilus.argent -= pirateChoisi.prix
                    nautilus.equipage.ajoutMarin(pirateChoisi)
                    nautilus.equipage.afficheMarins()

        selectionAchatPirate()
        print "On quitte la taverne"

    """""
    visiterTaverne()
    visiterTaverne()
    visiterTaverne()
    nautilus.equipage.afficheMarins()
    """""


    nautilus.initPosition()
    while nautilus.portActuel != "Istanbul":
        print " "

        #balbkaddscsc


        print "================================> PROCHAIN PORT <=================================="
        nautilus.bougePosition()
        print " "
        print " \/\/\/\/\/\/     Bienvenue à" , nautilus.portActuel, "    \/\/\/\/\/\/ "
        choixVisite = raw_input("Voulez-vous visiter la taverne du port ? (y/n)")
        if choixVisite == "y":
            visiterTaverne()

    print "On est arrivé à bon port"
