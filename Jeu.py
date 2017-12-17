# coding=utf-8
# Importation des bibliothèques fichiers
import random

import Carte
from Navigateur import Navigateur
from Navire import Navire
from Taverne import Taverne



# Fonction qui aléatoirement choisi un évènement (Combat, Sirène, Tempête, Avarie, Pas d'évènement)
def effectueTraverse(destination):
    numAction = random.randint(0, 10)
    # numAction = 4
    print 'numAction:', numAction

    if numAction in (0, 1, 2):
        combat()

    elif numAction == 3:
        sirene()

    elif numAction in (4, 5):
        destination = tempete()

    elif numAction == 6:
        destination = avarie()

    #Changement de la position du bateau et mise à jour des routes
    Carte.supprimerRoutes()
    Carte.creationRoute(destination)
    nautilus.actualisePosition(destination)

# Fonction qui simule un combat
def combat():
    print "\nNous voici en route mais malheureusement sur notre chemin se trouve un pavillon ennemi "
    print "--------- Combat ! ---------"
    print "Vous disposez de", nautilus.argent, "pièces d'or"

    # obtention de la force totale de notre navire
    forceNavire = nautilus.equipage.calculForce()

    # obtention aléatoire de la force du bateau ennemie par rapport à notre force
    forceEnnemi = ((random.randint(-100, 100)) * forceNavire / 100) + forceNavire

    # Calcule de la chance de victoire en fonction de notre force et de la force ennemie
    # (La chance de victoire repose le hasard d'avoir plus ou moins de la chance de victoire, il s'agit d'une sorte de pari)
    chanceEnnemi = (100 * forceEnnemi) / (forceNavire + forceEnnemi)
    print "La force de notre ennemi est de", forceEnnemi, ". Notre force est de", forceNavire

    # Choix de l'utilisateur de combattre ou non
    choixCombat = raw_input("Voulez-vous combattre ? (y/n)")
    if choixCombat == "y":

        # Condition pour voir si la chance de gagner et le nombre aléatoire est inférieur
        if random.randint(0,100) > chanceEnnemi:
            butin = random.randint(10, 200)
            print "Gagné !!!"
            nautilus.gagne(butin)
            print "Néanmoins vous avez subit quelques pertes..."
        # Couper des membres!
            nautilus.equipage.endommage()
            print "Après un combat acharné, continuons notre périble..."

        else:
            print "Perdu..."
            nautilus.equipage.endommage()

    else:
        print "Froussard, on continue la route !"

# Fonction qui simule une tempete: retourne un port et endommage le bateau
def sirene():
    marinPerdu = nautilus.equipage.enleveMarinAleatoirement()
    print "~~~~~    Une créature sort de l'eau, c'est une sirène!    ~~~~"
    print "La voici qui commence à chanter, ajoutant ce charme mysterieux à sa beauté naturelle."
    print "Vite, vous vous bouchez les oreilles pour ne pas succomber, les marins de votre equipage vous imite."
    print "Enfin, presque tous car " + marinPerdu.nom + " a déjà sauté dans la mer pour rejoindre la sirène."
    print "Le pauvre, vous devez l'abandonner à son sort."
    print "Le navire continue sa route et la sirène disparait après avoir commit son méfait."

# Fonction qui simule une tempete: retourne un port et endommage le bateau
def tempete():
    print "~~~~~    Il y a une tempête    ~~~~"
    portDeTempete = Carte.trouvePortAssezLoin()
    nautilus.equipage.endommage()
    print "Le navire dérive et se retrouve à ", portDeTempete
    return portDeTempete

# Fonction qui simule une avarie: retourne le port de depart
def avarie():
    obstacle = random.choice(('un écueil', 'une baleine', 'un bateau de pêcheurs'))
    print "~~~~~    A peine parti, le navire percute " + obstacle + "!   ~~~~"
    print "Vous devez rentrer au port pour effectuer des réparations"
    return nautilus.portActuel

# Fonction qui propose la dernière enigme du jeu lorsqu'on est à Istanbul
def tresor ():
    message = "BRAVO ! Te voilà arrivé Istambul !! \nTu es à deux doigts du but. Pour récupérer le trésor de Carthégius qui se trouve dans le temple d’Ephesus tu vas devoir passer par le gardien du Temple pour te guider. "
    message += "\n \nLe gardien : « Bonjour Moussaillon, on m’a dit que tu étais intéressé par le trésor. Je veux bien t’y emmener mais pour cela il faut que tu répondes à mon énigme ! "
    message += "\nEs-tu prêt, tu as trois chances sinon la malédiction du trésor s’abattra sur toi. "
    message += "\n« 5 marins sont venus avant toi, le premier et le second avait chacun une pièces d’or, le troisième avait 2 pièces, le quatrième 3 et le cinquième en avait 5. \nEt toi combien me proposes-tu de pièces ? »"
    reponse = raw_input(message)

    # L'utilisateur à 3 tentatives pour répondre à l'énigme
    tentative = 1
    while reponse != "8":
        if tentative < 3:
            reponse = raw_input("PFFF, Marin d’eaux douces ! Retente ta chance :")
            tentative += 1
        else:
            print "Mon dieu la malédiction s’abat sur toi. \nMalheureusement l'aventure s'arrête ici pour toi! Ne sois pas déçu, tu as tout de même pu parcourir la Méditerranée, et ça n'a pas de prix!!   "
            break
    if reponse == "8":
        print "Félicitations, tu as regardé le code ! Je te laisse repartir avec le trésor. Bon vent capitaine " + capitaine.nom

# Fonction qui propose les destinations et retourne la position choisie
def proposeDestination():
    destinationsPossible = Carte.trouveDestinationsProches()

    message = "Quel est le prochain port de destination ? (il vous reste " + str(nautilus.argent) + " pièces):"

    for index, destination in enumerate(destinationsPossible):
        message += "\n" + str(index + 1) + ". " + destination["port"] + "\t(" + str(destination["cout"]) + " pièces)"

    # L'utilisateur doit saisir un nombre entre 1 et 3
    choix = raw_input(message)
    while choix not in ("1", "2", "3"):
        choix = raw_input("Choix incorrect, tapez 1, 2 ou 3 :")

    destinationChoisie = destinationsPossible[int(choix) - 1]
    distanceEnMillesMarins = int(destinationChoisie["distance"] * 100 * 0.53)

    print "Vous avez décidé de vous rendre à " + destinationChoisie["port"]
    print "Le trajet est estimé à " + str(distanceEnMillesMarins) + " milles marins"
    print "Le coût du trajet sera de " + str(destinationChoisie["cout"]) + " pièces!"

    return destinationChoisie

# Fonction qui permet d'acquérir (gratuitement) 3 marins avant le départ
def achetePiratesDeDepart():
    print "A toi de composer ton équipage.\nVoici 10 pirates prêts à partir, tu dois en acheter 3 avant le départ."
    taverneDeDepart = Taverne()
    piratesDeDepart = taverneDeDepart.pirates
    choixPossibles = []
    choixPiratesDeDepart = []
    totalDepense = 0

    # Impression des pirates à choisirs
    for index, pirate in enumerate(piratesDeDepart):
        numeroChoix = str(index + 1)
        print numeroChoix + ".", pirate.nom + "\t\t(prix: " + str(pirate.prix) + " force: " + str(pirate.force) + ")"
        choixPossibles.append(numeroChoix)

    # Demande à l'utilisateur de saisir un pirate
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

    print "C'est le début de l'aventure, vos pirates sont financés par l'Institut de Geographie!"
    print "Vous économisez " + str(totalDepense) + " pièces, profitez-en, cela n'arrive qu'une fois!"

    nautilus.equipage.afficheMarins()

# Fonction qui visite une taverne
def visiteTaverne():
    #Gestion de l'argent au debut de la taverne
    taverneAPirate = Taverne()
    taverneAPirate.visite(nautilus.argent)

    # Après la visite, on utilise taverneAPirate.depenseVisiteur pour mettre a jour l'argent du nautilus
    if taverneAPirate.depenseVisiteur > 0:
        nautilus.depense(taverneAPirate.depenseVisiteur)

    elif taverneAPirate.depenseVisiteur < 0:
        nautilus.gagne(-taverneAPirate.depenseVisiteur)

    # Ensuite, on utilise taverneAPirate.panierMarins pour ajouter les marins à l'équipage du nautilus, si besoin
    if len(taverneAPirate.panierMarins) > 0:
        for marin in taverneAPirate.panierMarins:
            nautilus.equipage.ajoutMarin(marin)

        nautilus.equipage.afficheMarins()



if __name__ == "__main__":
    #Impréssion du message de début de jeu
    messageDebut = "Bien le bonjour à toi jeune Corsaire, \n"
    messageDebut += "J’espère que tu es en pleine forme car à partir de maintenant tu vas devoir faire tes preuves !!  \n"
    messageDebut += "Tu es ici pour prendre connaissances de ta mission. Tu dois te rendre à Istambul pour dérober le trésor de Carthégius. \n"
    messageDebut += "C’est ici à Rabat que tout va commencer. \nPour débuter, commence par choisir le nom de ton capitaine :"

    #Création du capitaine
    nomCapitaine = raw_input(messageDebut)
    capitaine = Navigateur(nomCapitaine, 10, 12)

    nautilus = Navire("Nautilus", 1000, capitaine)
    nautilus.initPosition("Rabat")

    #Exécution de la fonction permettant d'acquérir 3 marins au début du jeu
    achetePiratesDeDepart()

    print "Maintenant, nous partons à l'aventure"

    # Exécution lorsque le bateau n'est pas encore à Istanbul
    while nautilus.portActuel != "Istanbul":
        print "\n================================> PROCHAIN PORT <=================================="
        portDeDestination = proposeDestination()
        nautilus.depense(portDeDestination["cout"])

        # on sort de la boucle si le joueur a dépensé trop d'argent
        if nautilus.argent < 0:
            break

        #Exécution d'un évenement (ou non ) durée la traversée
        effectueTraverse(portDeDestination["port"])

        print "\n =======================>  BIENVENUE à " + nautilus.portActuel.upper() + "  <======================="

        # on sort de la boucle si on est à Istanbul
        if nautilus.portActuel == "Istanbul":
            break

        # On demande si l'utilisateur veut visiter la taverne
        choixVisite = raw_input("Voulez-vous visiter la taverne du port ? (y/n)")
        while choixVisite not in ['y', 'n']:
            choixVisite = raw_input("Choix incorrect!")

        if choixVisite == "y":
            visiteTaverne()

    # Action lorsque le beateau arrive à Istanbul
    if nautilus.portActuel == "Istanbul":
        tresor()

    # Action lorsqu'il n'y a plus d'argent aprés avoir chosie un port
    if nautilus.argent < 0:
        print "Vous avez une gestion des comptes lamentable, vos marins vous haissent, et malheureusement, l'aventure s'achève ici!" \

