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


    print "1"
    nomCapitaine = raw_input("Choisi votre nom de capitaine : ")
    marins = N.Navigateur(nomCapitaine, 10, 12)
    print "2"
    equipage = [marins]
    print "3"
    nautilus = B.Navire("Nautilus", 100000, "Rabat", equipage)
    print "4"
    equipage = E.Equipage(N.Navigateur("Blabla", 10, 10))


    taverneAPirate = T.Taverne(nomDePirate, prenomDePirate)
    listePirate = T.creationListePirateAChoisir(taverneAPirate, 3)

    for i in listePirate:
        print i.nom, i.argent, i.force
    marins = N.Navigateur(nomCapitaine, 10, 12)
    nautilus.initPosBateau()
    nautilus.navire.equipage.afficheMarins()
    choixPirate = raw_input("choisir le pirate")
    equipage.ajoutMarin(listePirate[choixPirate]) #chxPirate -> indice du pirate choisit dans la liste

    while B.nautilus.argent > -1:
        B.nautilus.bougerBateau()
    else:
        finPerdu()
        print "Vous n'avez plus d'argent"