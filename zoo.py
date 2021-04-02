
from numpy.ma.core import append

from Animal import Animal


class Zoo:
    liste_animaux_zoo=[]
    def __init__(self, liste_animaux_zoo):
        self.liste_animaux_zoo=[]
        for elm_Animal in liste_animaux_zoo:
            if isinstance(elm_Animal, Animal) == False:
                raise TypeError()
            else:
                self.liste_animaux_zoo.append(elm_Animal)
        
    def add_animal(self, animal):#ajouter un objet de type Animal à une instance de Zoo.
        self.liste_animaux_zoo.append(animal)
          
          

    # Operator overloading: rajouter un support pour l’opération “+”entre objets de type Zoo.
    def __add__(self, other):        
        if isinstance(other, Zoo):            
            return Zoo(self.liste_animaux_zoo+other.liste_animaux_zoo)       
        else:           
            return None

# PROGRAMME PRINCIPAL
chat = Animal(poids=5, taille=10)
chien = Animal(poids=4,taille=6)
lapin = Animal(poids=1,taille=4)
tigre = Animal(poids=100,taille=3)
lion = Animal(poids=150,taille=4)

zoo_domestique = Zoo([chat, chien])
zoo_domestique.add_animal(lapin)
#liste_animaux_zoo3=
#print(len(zoo_domestique.liste_animaux_zoo))
#print('\n'. join ([str(i) for i in zoo_domestique.liste_animaux_zoo]))

    
zoo_domestique = Zoo([chat, chien])
zoo_sauvage = Zoo([tigre, lion])
#zoo=zoo_domestique.__add__(zoo_sauvage)
zoo=zoo_domestique+zoo_sauvage
print('\n'. join ([str(i) for i in zoo.liste_animaux_zoo]))
#print(chat)
#animals = ['cat', 'dog', 'rabbit']
#animals.append('guinea pig')
#print('Updated animals list: ', animals)