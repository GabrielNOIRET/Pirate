# coding=utf-8
# Importation des bibliothèques fichiers
import Carte
import Navire as B
import Equipage as E
import Taverne as T
import Navigateur as N
import random


# Fonction qui aléatoirement choisi un évènement (Combat, Sirène, Tempête, Avarie, Pas d'évènement)
def effectueTraverse(navire, destination):
    numAction = random.randint(0, 10)
    numAction = 3

    if numAction in (1, 2):
        combat(navire)

    elif numAction == 3:
        sirene(navire)

    elif numAction == 4:
        destination = tempete(navire)

    elif numAction == 5:
        destination = avarie(navire)

    Carte.supprimerRoutes()
    Carte.creationRoute(destination)
    nautilus.actualisePosition(destination)


# Fonction qui simule un combat
def combat(navire):
    print "\nNous voici en route mais malheureusement sur notre chemin se trouve un pavillon ennemi "
    print "--------- Combat ! ---------"
    print "Vous disposez de", navire.argent, "pièces d'or"

    # obtention de la force totale de notre navire
    forceNavire = navire.equipage.calculForce()

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
        #if True:
            butin = random.randint(10, 200)
            print "Gagné !!!"
            navire.gagne(butin)
            print "Néanmoins vous avez subit quelques pertes..."
        # Couper des membres!
            navire.equipage.endommage()
            print "Après un combat acharné, continuons notre périble..."


        else:
            print "Perdu..."
            navire.equipage.endommage()

    else:
        print "Froussard, on continue la route !"

# Fonction qui simule une tempete: retourne un port et endommage le bateau
def sirene(navire):
    marinPerdu = navire.equipage.enleveMarinAleatoirement()
    print "~~~~~    Une créature sort de l'eau, c'est une sirène!    ~~~~"
    print "La voici qui commence à chanter, ajoutant ce charme mysterieux à sa beauté naturelle."
    print "Vite, vous vous bouchez les oreilles pour ne pas succomber, les marins de votre equipage vous imite."
    print "Enfin, presque tous car " + marinPerdu.nom + " a déjà sauté dans la mer pour rejoindre la sirène."
    print "Le pauvre, vous devez l'abandonner à son sort."
    print "Le navire continue sa route et la sirène disparait après avoir commit son méfait."

# Fonction qui simule une tempete: retourne un port et endommage le bateau
def tempete(navire):
    print "~~~~~    Il y a une tempête    ~~~~"
    portDeTempete = Carte.trouvePortAssezLoin()
    #Carte.supprimerRoutes()
    #Carte.positionneBateau(portDeTempete)
    navire.equipage.endommage()
    #TODO  changer texte
    print "Le navire derive et se retrouve à ", portDeTempete
    return portDeTempete

# Fonction qui simule une avarie: retourne le port de depart
def avarie(navire):
    obstacle = random.choice(('un eceuil', 'une baleine', 'un bateau de pecheurs'))
    print "~~~~~    A peine parti, le navire percute " + obstacle + "!   ~~~~"
    print "Vous devez rentrer au port pour effectuer des reparations"
    return navire.portActuel

# Fonction qui propose les destinations et retourne la position choisie
def proposeDestination():
    destinationsPossible = Carte.trouveDestinationsProches()

    message = "Quel est le prochain port de destination ? :"

    for index, destination in enumerate(destinationsPossible):
        message += "\n" + str(index + 1) + ". " + destination["port"] + "\t(" + str(destination["cout"]) + " pieces)"

    choix = raw_input(message)
    while choix not in ("1", "2", "3"):
        choix = raw_input("Choix incorrect, tapez 1, 2 ou 3 :")

    destinationChoisie = destinationsPossible[int(choix) - 1]

    return destinationChoisie


def achetePiratesDeDepart():
    print "A toi de composer ton équipage.\nVoici 10 pirates prêts à partir, tu dois en acheter 3 avant le départ."
    taverneDeDepart = T.Taverne()
    piratesDeDepart = taverneDeDepart.pirates
    choixPossibles = []
    choixPiratesDeDepart = []
    totalDepense = 0

    for index, pirate in enumerate(piratesDeDepart):
        numeroChoix = str(index + 1)
        print numeroChoix + ".", pirate.nom + "\t\t(prix: " + str(pirate.prix) + " force: " + str(pirate.force) + ")"
        choixPossibles.append(numeroChoix)

    for nb in range(3):
        choixPirate = raw_input("Quel pirate voulez-vous ? (" + str(3 - len(choixPiratesDeDepart)) + " restants)")
        while choixPirate not in choixPossibles or choixPirate in choixPiratesDeDepart:
            messageChoixIncorrect = "Choix incorrect!"
            if choixPirate in choixPiratesDeDepart:
                messageChoixIncorrect = "Déjà choisi!"
            choixPirate = raw_input(messageChoixIncorrect)

        choixPiratesDeDepart.append(choixPirate)

        pirateChoisi = piratesDeDepart[int(choixPirate) - 1]
        totalDepense += pirateChoisi.prix
        nautilus.equipage.ajoutMarin(pirateChoisi)

    nautilus.depense(totalDepense)
    nautilus.equipage.afficheMarins()


def visiteTaverne():
    taverneAPirate = T.Taverne()
    taverneAPirate.visite(nautilus.argent)

    # Après la visite, on utilise taverneAPirate.depenseVisiteur pour mettre a jour l'argent du nautilus
    if taverneAPirate.depenseVisiteur > 0:
        nautilus.depense(taverneAPirate.depenseVisiteur)

    elif taverneAPirate.depenseVisiteur < 0:
        nautilus.gagne(taverneAPirate.depenseVisiteur)

    # Ensuite, on utilise taverneAPirate.panierMarins pour ajouter les marins à l'équipage du nautilus, si besoin
    if len(taverneAPirate.panierMarins) > 0:
        for marin in taverneAPirate.panierMarins:
            nautilus.equipage.ajoutMarin(marin)

        nautilus.equipage.afficheMarins()



if __name__ == "__main__":
    messageDebut = "Bien le bonjour à toi jeune Corsaire, \n"
    messageDebut += "J’espère que tu es en pleine forme car à partir de maintenant tu vas devoir faire tes preuves !!  \n"
    messageDebut += "Tu es ici pour prendre connaissances de ta mission. Tu dois te rendre à Istambul pour dérober le trésor de Carthégius. \n"
    messageDebut += "C’est ici à Rabat que tout va commencer. \nPour débuter, commence par choisir le nom de ton capitaine :"

    nomCapitaine = raw_input(messageDebut)
    capitaine = N.Navigateur(nomCapitaine, 10, 12)
    nautilus = B.Navire("Nautilus", 1000, capitaine)

    achetePiratesDeDepart()

    print "Maintenant, nous partons à l'aventure"


    nautilus.initPosition()
    while nautilus.portActuel != "Istanbul":
        print "\n================================> PROCHAIN PORT <=================================="
        portDeDestination = proposeDestination()
        print "Vous avez décidé de vous rendre a " + portDeDestination["port"] + ", le trajet est estime a " + str((int(portDeDestination["distance"])*100)*0.53) + " milles marins, vous depensez " + str(portDeDestination["cout"]) + " pieces!"

        nautilus.depense(10000)
        #nautilus.depense(portDeDestination["cout"])

        effectueTraverse(nautilus, portDeDestination["port"])
        if nautilus.argent < 0:
            print "Vous n'avez plus d'argent.."
            #TODO message plus d'argent
            break

        print "\n \/\/\/\/\/\/     Bienvenue à" , nautilus.portActuel,"    \/\/\/\/\/\/ "
        choixVisite = raw_input("Voulez-vous visiter la taverne du port ? (y/n)")
        while choixVisite not in ['y', 'n']:
            choixVisite = raw_input("Choix incorrect!")
        if choixVisite == "y":
            visiteTaverne()

    if nautilus.portActuel == "Istanbul":
        print "On est arrivé à bon port"
        #TODO Ecrire texte arrivée

    else:
        print "Perdu"
