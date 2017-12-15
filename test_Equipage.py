from Equipage import Equipage
from Navigateur import Navigateur

import random

listDeMarins = [
    Navigateur("Tristan", 20, 10),
    Navigateur("Gabriel", 20, 10),
    Navigateur("Capucine", 20, 10),
    Navigateur("Laurent", 20, 10),
]

monEquipage = Equipage(listDeMarins)

monEquipage.ajoutMarin(Navigateur("Babar", 20, 10))

monEquipage.endommage()
monEquipage.endommage()
monEquipage.endommage()
monEquipage.endommage()




# print monEquipage

# for i in range(0,20,1):
#     print random.randint(0, 10)
