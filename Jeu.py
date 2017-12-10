# coding=utf-8
import Navire as B
import Equipage as E
import Taverne as T
import Navigateur as N

def finPerdu():
    print "Vous avez perdu"
    exit(0)

def finGagnee():
    print "Vous avez gagné"
    exit(0)

def arriveeIstanbul():
    print "Vous etes arrivé a Istanbul"
    finGagnee()

if __name__ == "__main__":

    #listAccident = ["bras", "jambe", "yeux"]
    nomDePirate = ["Bonny", "Jack", "Teach", "Drake", "Morgan", "Nau", "Read"]
    prenomDePirate = ["Anne", "Calico", "Edward", "Francis", "Henry", "Jean", "Mary"]



    nomCapitaine = raw_input("Choisi votre nom de capitaine : ")
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
        print "Il vous reste :",nautilus.argent,"pieces d'or"
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
                    print "Ce pirate est trop cher !"
                    selectionAchatPirate()
                else:
                    nautilus.argent -= pirateChoisi.prix
                    nautilus.equipage.ajoutMarin(pirateChoisi)
                    nautilus.equipage.afficheMarins()

        selectionAchatPirate()
        print "on quitte la taverne"

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
        choixVisite = raw_input("Voulez-vous visiter la taverne ? (y/n)")
        if choixVisite == "y":
            visiterTaverne()

    print "on est arrivé"
