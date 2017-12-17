# coding=utf-8
from Taverne import Taverne


taverneTest = Taverne()
taverneTest.visite(1000)

print "argent restant: " + str(taverneTest.argentVisiteur)
print "marins achetés: ", taverneTest.panierMarins