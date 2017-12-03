class Navire(object):

    def __init__(self, nom, listeMarins):
        self.nom = nom  # Ajout du nom du navire
        self.equipage = Equipage(
            listeMarins)  # On demande la liste equipage a partir de la classe equipe qui prend attribut "listemaris"

    def combat(self, ennemi):
        print "combat le bateau ennemi ! "
