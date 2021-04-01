
from numpy.ma.core import append

from Animal import Animal


class Zoo:
    def __init__(self, liste_animaux_zoo):
        self.liste_animaux_zoo=[]
        for Animal in liste_animaux_zoo:
            if isinstance(Animal, Animal) == False:
                raise TypeError()
            else:
                self.liste_animaux_zoo.append(Animal)
                return liste_animaux_zoo()



# PROGRAMME PRINCIPAL

liste_animaux_zoo = ["chat", "chien"]

lapin = Animal(3, 0.5)
liste_animaux_zoo.append(lapin)



