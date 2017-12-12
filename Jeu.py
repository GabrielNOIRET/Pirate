# coding=utf-8
import Navire as B
import Equipage as E
import Taverne as T
import Navigateur as N
import random

def finPerdu():
    print "Vous avez perdu"
    exit(0)

def finGagnee():
    print "Vous avez gagné"
    exit(0)

def arriveeIstanbul():
    print "Vous êtes arrivé a Istanbul"
    finGagnee()



def action(leNavire):
    numAction = random.randint(0, 10)
    numAction = 0

    if numAction < 3:
        combat(leNavire)

    elif numAction == 3:
        print "Sirène"

    elif numAction == 4:
        print "Tempête"




def combat(unNavire):
    print "--------- Combat ! ---------"
    print unNavire.argent

    forceNavire = unNavire.equipage.calculForce()
    forceEnnemi = ((random.randint(-100, 100)) * forceNavire / 100) + forceNavire
    chanceEnnemi = (100 * forceEnnemi) / (forceNavire + forceEnnemi)
    print "La force de notre ennemi est de", forceEnnemi, ". Notre force est de", forceNavire
    choixCombat = raw_input("Voulez-vous combattre ? (y/n)")
    if choixCombat == "y":
        if random.randint(0,100) > chanceEnnemi:
            butin = random.randint(10, 200)
            print "Gagné!, vous remportez", butin,"pièces d'or"
            unNavire.argent += butin
        else:
            print "Perdu"
            #for pertes in range(random.randint(0, len(nautilus.equipage.listeMarins))):
    print unNavire.argent





if __name__ == "__main__":

    #listAccident = ["bras", "jambe", "yeux"]
    nomDePirate = ["Bonny", "Jack", "Teach", "Collaart", "Morgan", "Nau", "Read", "Riskinner", "Oxenham", "Compaan", "Cavendish", "Mainwaring", "Essex", "Morris", "Braziliano", "Sawkins", "Anstis", "Culliford", "Henríquez", "Neumann"]
    prenomDePirate = ["William", "Calico", "Edward", "John", "Henry", "Jean", "Mary", "James", "Isaac", "Jan", "Vincenzo", "Jacquotte", "Cornelius", "George", "Thomas", "Lars", "Miguel", "Edward", "Christopher", "Mary", "Flora"]



    nomCapitaine = raw_input("Vous pouvez choisir le nom de votre capitaine : ")
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
        print "Il vous reste :",nautilus.argent,"pièces d'or"
        taverneAPirate = T.Taverne(nomDePirate, prenomDePirate)
        listePirate = T.creationListePirateAChoisir(taverneAPirate, 3)

        print "Voici les pirates disponibles : "
        for index, pirate in enumerate(listePirate):
            print index + 1, "-", pirate.nom, "(prix: ", pirate.prix, "force: ", pirate.force,")"

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



    """
    while B.nautilus.argent > -1:
        B.nautilus.bougerBateau()
    else:
        finPerdu()
       print "Vous n'avez plus d'argent"
    """

    nautilus.initPosition()
    while nautilus.portActuel != "Istanbul":
        print "================================"
        nautilus.bougePosition()
        print "Bienvenue à ", nautilus.portActuel
        choixVisite = raw_input("Voulez-vous visiter la taverne du port ? (y/n)")
        if choixVisite == "y":
            visiterTaverne()

    print "On est arrivé à bon port"
