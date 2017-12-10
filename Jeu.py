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
    nautilus = B.Navire("Nautilus", 100000, "Rabat", debutListeMarins)
    #equipage = E.Equipage(N.Navigateur("Blabla", 10, 10))


    #taverneAPirate = T.Taverne(nomDePirate, prenomDePirate)
    #listePirate = T.creationListePirateAChoisir(taverneAPirate, 3)



    capitaine = N.Navigateur(nomCapitaine, 10, 12)
    nautilus.initPosBateau()
    nautilus.equipage.afficheMarins()
    #print "Voici les pirates disponibles : "
    #for index, pirate in enumerate(listePirate):
     #   print index+1, ".", pirate.nom, "Cout: ", pirate.argent, "Force: ", pirate.force

    def saisieAjoutMarin ():
        taverneAPirate = T.Taverne(nomDePirate, prenomDePirate)
        listePirate = T.creationListePirateAChoisir(taverneAPirate, 3)

        print "Voici les pirates disponibles : "
        for index, pirate in enumerate(listePirate):
            print index + 1, ".", pirate.nom, "Cout: ", pirate.argent, "Force: ", pirate.force

        choixPirate = raw_input("choisir le pirate")
        # TODO: verifier que l'utilisateur rentre bien un nombre
        nautilus.equipage.ajoutMarin(listePirate[int(choixPirate) - 1])

    saisieAjoutMarin()
    saisieAjoutMarin()
    saisieAjoutMarin()

    nautilus.equipage.afficheMarins()

    while B.nautilus.argent > -1:
        B.nautilus.bougerBateau()
    else:
        finPerdu()
        print "Vous n'avez plus d'argent"