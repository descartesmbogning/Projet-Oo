class Animal(): # créer une classe Animal
    """
    Création d'un zoo virtuel en python
    """
    poids = 0    
    taille = 0 
    
    def __init__(self, poids, taille):
        self.animal_poids = poids
        self.animal_taille = taille
        
    def se_deplacer(self):    #Ajoutez une méthode se_deplacer( ) qui pour le moment ne fait rien.
        pass 
    

class Serpent(Animal):  # classe serpent qui hérite de la classe animal
    def se_deplacer(self):    #redefinir la méthode se_deplacer( ) pour serpent.
       print('Je rampe')

class Oiseau(Animal):  # classe Oiseau qui hérite de la classe animal
    def se_deplacer(self):    #redefinir la méthode se_deplacer( ) pour Oiseau.
        print('Je vole')

    



#instanciez cet objet. Faites un print de ses attributs.  
python = Animal(80, 2) 
print(f"Le poids de l'animal est de : {python.animal_poids}")
print(f"La taille de l'animal est de : {python.animal_taille}")


#Instanciez maintenant ces deux objets dans le
#programme principal et appelez la méthode se_deplacer( ) pour chacun de ces
#objets.
#obj_animal = Animal()
python= Serpent(10, 5)
rosignol = Oiseau(2, 1)
print(f"Je suis monsieur python, serpent, {python.se_deplacer()}")
print(f"Je suis madame la rosignol, l'oiseau, {rosignol.se_deplacer()}")





