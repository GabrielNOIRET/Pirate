# -*- coding: utf-8 -*-
# Importation des bibliothèques
import psycopg2


try:
    conn = psycopg2.connect(
        "dbname='reyman64_cartha' user='reyman64_cartha' host='web564.webfaction.com' password='carthageo'")
    conn.autocommit = True
except:
    print "I am unable to connect to the database"  # Si la base ne se connecte pas
cur = conn.cursor()


class Navire(object):
    def __init__(self, n, a, pd):
        self.nom = n
        self.argent = a
        self.portDepart = pd

    def initPosBateau(self):
        print "On va initialiser la position du bateau"
        cur.execute("""UPDATE exo2016.bateaux SET geom = (SELECT geom FROM exo2016.ports WHERE "City" = '"""+ self.portDepart +"""') WHERE nom = 'Nautilus';""")

    def bougerBateau(self):
        # Voir les 3 ports les plus proches
        requete = """SELECT "City", ST_Distance(geom, (SELECT geom FROM exo2016.bateaux WHERE nom = 'Nautilus')) AS distance FROM exo2016.ports ORDER BY distance ASC LIMIT 3 OFFSET 1;"""
        cur.execute(requete)
        # Affiche le tableau de la requete
        rows = cur.fetchall()

        nomdest = []
        coutdest = []
        def propositionDestination():
            nbl = 0
            for row in rows:
                nbl += 1
                print nbl,"- Pour aller à", row[0], ', ça va couter', int(10 * row[1]), "pieces d'or"
                nomdest.append(row[0])
                coutdest.append(row[1])
        propositionDestination()

        # Supprimer ancienne route
        def supprimerRoutes():
            requete_suproute = """DELETE FROM exo2016.routes WHERE idbinome = '6';"""
            cur.execute(requete_suproute)
        supprimerRoutes()

        # Creation des routes
        def creationRoute(portEscale):
            requete_creatroute = """INSERT INTO exo2016.routes (id, idbinome, geom) VALUES (DEFAULT, '6', ST_MakeLine((SELECT geom FROM exo2016.bateaux WHERE nom = 'Nautilus'),(SELECT geom FROM exo2016.ports WHERE "City" = '""" + portEscale + """')));"""
            cur.execute(requete_creatroute)

        saisie = False
        while saisie == False:
            portEscale = raw_input("Quel est le prochain port :")
            portEscale = portEscale.replace(' ','')
            print "On va bouger le bateau"
            if portEscale in ("1","2","3"):
                creationRoute(nomdest[int(portEscale)-1])
                coutdest = int(coutdest[int(portEscale) - 1])*10
                portEscale = nomdest[int(portEscale)-1]
                requete_nvpos = """UPDATE exo2016.bateaux SET geom = (SELECT geom FROM exo2016.ports WHERE "City" = '""" + portEscale + """') WHERE nom = 'Nautilus';"""
                cur.execute(requete_nvpos)
                print "La nouvelle position du bateau est", portEscale
                saisie = True
            elif portEscale in nomdest:
                creationRoute(portEscale)
                for i in range(len(nomdest)):
                    if portEscale == nomdest[i]:
                        coutdest = int(coutdest[i])*10
                requete_nvpos = """UPDATE exo2016.bateaux SET geom = (SELECT geom FROM exo2016.ports WHERE "City" = '""" + portEscale + """') WHERE nom = 'Nautilus';"""
                cur.execute(requete_nvpos)
                saisie = True
            else:
                propositionDestination()
                print "Ressaisie la destination"
                saisie = False

        def coutdestination(coutdest):
            self.argent -= coutdest
            print "Vous êtes arrivé a", portEscale, ", il vous reste,",self.argent, "pieces d'or"
        coutdestination(coutdest)


nautilus = Navire("Nautilus", 100,"Rabat")
nautilus.initPosBateau()

