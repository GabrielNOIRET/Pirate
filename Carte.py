# coding=utf-8
# Import des bibliothèques fichiers
import psycopg2

# Connection et test de la base de données
try:
    conn = psycopg2.connect(
        "dbname='reyman64_cartha' user='reyman64_cartha' host='web564.webfaction.com' password='carthageo'")
    conn.autocommit = True
except:
    # Si la base ne se connecte pas
    print "I am unable to connect to the database"
cur = conn.cursor()


# Fonction qui affiche et liste les 3 ports les plus proches
def trouveDestinationsProches():
    # Trouver les 3 ports les plus proches
    requete = """SELECT "City", ST_Distance(geom, (SELECT geom FROM exo2016.bateaux WHERE nom = 'Nautilus')) AS distance FROM exo2016.ports ORDER BY distance ASC LIMIT 3 OFFSET 1;"""
    cur.execute(requete)
    rows = cur.fetchall()

    destinations = []
    for index, row in enumerate(rows):
        destination = {
            "port": row[0],
            "distance": row[1],
            "cout": int(row[1] * 10)
        }
        destinations.append(destination)

    return destinations


# Supprimer ancienne route
def supprimerRoutes():
    requete_suproute = "DELETE FROM exo2016.routes WHERE idbinome = '6';"
    cur.execute(requete_suproute)


# Creation des routes
def creationRoute(portEscale):
    requete_creatroute = """INSERT INTO exo2016.routes (id, idbinome, geom) VALUES (DEFAULT, '6', ST_MakeLine((SELECT geom FROM exo2016.bateaux WHERE nom = 'Nautilus'),(SELECT geom FROM exo2016.ports WHERE "City" = '""" + portEscale + """')));"""
    cur.execute(requete_creatroute)


# Positionnement du bateau sur la DB
def positionneBateau(position):
    cur.execute("""UPDATE exo2016.bateaux SET geom = (SELECT geom FROM exo2016.ports WHERE "City" = '""" + position + """') WHERE nom = 'Nautilus';""")
