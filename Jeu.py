# coding=utf-8
import psycopg2
import Navire

def finPerdu():
    print "Vous avez perdu"

if __name__ == "__main__":


    while Navire.nautilus.argent > -1:
        Navire.nautilus.bougerBateau()


            # -----------------
        try:
            conn = psycopg2.connect(
                "dbname='reyman64_cartha' user='reyman64_cartha' host='web564.webfaction.com' password='carthageo'")
            conn.autocommit = True
        except:
            print "I am unable to connect to the database"  # Si la base ne se connecte pas
        cur = conn.cursor()
        requete = """SELECT geom FROM exo2016.bateaux WHERE nom = 'Nautilus'"""
        cur.execute(requete)
        print cur.execute(requete)


    else:
        finPerdu()
        print "Vous n'avez plus d'argent"