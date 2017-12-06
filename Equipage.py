class Equipage(object):
    def __init__(self, listeMarins):
        self.listeMarins = listeMarins

    def ajoutMarin(self, marinChoisi):
        self.listeMarins.append(marinChoisi)