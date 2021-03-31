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
    

class Oiseau(Animal):  # classe Oiseau qui hérite de la classe animal
    def se_deplacer(self):    #redefinir la méthode se_deplacer( ) pour Oiseau.
        return 'Je vole'

    

#Instanciez maintenant ces deux objets dans le
#programme principal et appelez la méthode se_deplacer( ) pour chacun de ces
#objets.
rosignol = Oiseau(2, 1)
print(f"Je suis madame la rosignol, l'{type(rosignol)}, {rosignol.se_deplacer()}")





