
from numpy.ma.core import append

from Animal import Animal


class Zoo:
    liste_animaux_zoo1=[]
    liste_animaux_zoo2=[]
    liste_animaux_zoo=[]
    liste_animaux_zoo=liste_animaux_zoo1 + liste_animaux_zoo2
    
    def __init__(self, liste_animaux_zoo):
        self.liste_animaux_zoo=[]
        for elm_Animal in liste_animaux_zoo:
            if isinstance(elm_Animal, Animal) == False:
                raise TypeError()
            else:
                self.liste_animaux_zoo.append(str(Animal))
               

    def __str__(self):
        return f"L animal pèse {self.poids}kg et et à une taille de {self.__taille}"

# PROGRAMME PRINCIPAL
chat = Animal(poids=5, taille=10)
chien = Animal(poids=4,taille=6)
lapin = Animal(poids=1,taille=4)

liste_animaux_zoo = [chat, chien]

liste_animaux_zoo.append(lapin)
print(liste_animaux_zoo)




#animals = ['cat', 'dog', 'rabbit']
#animals.append('guinea pig')
#print('Updated animals list: ', animals)
