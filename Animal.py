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
     



#instanciez cet objet. Faites un print de ses attributs.  
python = Animal(80, 2) 
#print(f"Le poids de l'animal est de : {python.animal_poids}")
#print(f"La taille de l'animal est de : {python.animal_taille}")





